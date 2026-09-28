import math
import os
from typing import Dict, List, Optional, Tuple
import pygame
from fly_in.graph import Graph
from fly_in.planner import Plan, Step
from fly_in.simulation import Simulation
from fly_in.zone import Zone, ZoneType


RGB = Tuple[int, int, int]
Point = Tuple[float, float]

COLORS: Dict[str, RGB] = {
    "red": (220, 50, 47), "green": (46, 160, 67), "blue": (38, 110, 220),
    "yellow": (235, 200, 40), "orange": (240, 140, 30),
    "cyan": (40, 200, 210), "purple": (140, 70, 200),
    "magenta": (210, 60, 180), "pink": (240, 130, 190),
    "gray": (130, 130, 130), "grey": (130, 130, 130),
    "black": (60, 60, 60), "white": (235, 235, 235),
    "brown": (140, 90, 50), "gold": (230, 180, 30),
    "lime": (140, 220, 60), "maroon": (128, 30, 40),
    "darkred": (150, 20, 20), "crimson": (200, 20, 60),
    "violet": (170, 110, 230), "rainbow": (255, 120, 200),
}
DEFAULT_ZONE: RGB = (110, 120, 135)
BACKGROUND: RGB = (24, 26, 32)
EDGE: RGB = (90, 96, 110)
TEXT: RGB = (225, 228, 235)
MUTED: RGB = (140, 146, 160)
DRONE: RGB = (250, 250, 250)

WIDTH, HEIGHT = 1440, 810
MARGIN = 80
MAX_STRETCH = 1.8
HUD_HEIGHT = 70
FOOTER_HEIGHT = 30
TURN_SECONDS = 0.8
FPS = 60


def zone_color(zone: Zone) -> RGB:
    """Return the RGB color of a zone (grey for unknown names)."""
    if zone.color is None:
        return DEFAULT_ZONE
    return COLORS.get(zone.color.lower(), DEFAULT_ZONE)


class Layout:
    """Convert map coordinates into window pixels."""

    def __init__(self, graph: Graph) -> None:
        """Fit every zone inside the drawing area.

        Each axis may be stretched up to MAX_STRETCH times more than
        the other, so long and flat maps still use the whole window.
        """
        xs = [zone.x for zone in graph.zones.values()]
        ys = [zone.y for zone in graph.zones.values()]
        self.min_x, self.max_y = min(xs), max(ys)
        span_x = max(max(xs) - self.min_x, 1)
        span_y = max(self.max_y - min(ys), 1)
        area_w = WIDTH - 2 * MARGIN
        area_h = HEIGHT - HUD_HEIGHT - FOOTER_HEIGHT - 2 * MARGIN
        uniform = min(area_w / span_x, area_h / span_y)
        self.scale_x = min(area_w / span_x, uniform * MAX_STRETCH)
        self.scale_y = min(area_h / span_y, uniform * MAX_STRETCH)
        self.off_x = MARGIN + (area_w - span_x * self.scale_x) / 2
        self.off_y = (HUD_HEIGHT + MARGIN
                      + (area_h - span_y * self.scale_y) / 2)
        spacing = min(self.scale_x, self.scale_y)
        self.radius = int(max(12, min(30, spacing * 0.28)))

    def point(self, zone: Zone) -> Point:
        """Return the pixel center of a zone (map y grows upwards)."""
        return (self.off_x + (zone.x - self.min_x) * self.scale_x,
                self.off_y + (self.max_y - zone.y) * self.scale_y)


class Timeline:
    """Know where every drone is drawn at any moment of the simulation."""

    def __init__(self, graph: Graph, plans: List[Plan],
                 layout: Layout) -> None:
        """Precompute the drone positions at the end of every turn."""
        self.graph = graph
        self.plans = plans
        self.layout = layout
        self.nb_turns = Simulation(plans).nb_turns
        self.frames = [self._frame(turn)
                       for turn in range(self.nb_turns + 1)]

    def _step(self, plan: Plan, turn: int) -> Step:
        """Return the step of a plan, staying on the last one after it."""
        return plan[min(turn, len(plan) - 1)]

    def _frame(self, turn: int) -> Dict[int, Tuple[Point, bool]]:
        """Return {drone: (pixel, visible)} at the end of a turn.

        Drones in start or end are hidden (a counter is shown instead);
        several drones in one zone are spread around its center.
        """
        groups: Dict[str, List[int]] = {}
        frame: Dict[int, Tuple[Point, bool]] = {}
        for drone, plan in enumerate(self.plans, start=1):
            step = self._step(plan, turn)
            if step.link is None:
                groups.setdefault(step.zone, []).append(drone)
                continue
            a = self.layout.point(self.graph.zones[step.link.zone_a])
            b = self.layout.point(self.graph.zones[step.link.zone_b])
            frame[drone] = (((a[0] + b[0]) / 2, (a[1] + b[1]) / 2), True)
        for name, drones in groups.items():
            zone = self.graph.zones[name]
            cx, cy = self.layout.point(zone)
            hidden = zone is self.graph.start or zone is self.graph.end
            spread = self.layout.radius * 0.55 if len(drones) > 1 else 0
            for i, drone in enumerate(drones):
                angle = 2 * math.pi * i / len(drones) - math.pi / 2
                pos = (cx + spread * math.cos(angle),
                       cy + spread * math.sin(angle))
                frame[drone] = (pos, not hidden)
        return frame

    def drones_at(self, time: float) -> List[Tuple[int, Point]]:
        """Return the visible drones at a (fractional) time."""
        turn = min(int(math.ceil(time)), self.nb_turns)
        prev = max(turn - 1, 0)
        ratio = 1.0 if turn == prev else time - prev
        ratio = ratio * ratio * (3 - 2 * ratio)
        result: List[Tuple[int, Point]] = []
        for drone in range(1, len(self.plans) + 1):
            (x0, y0), vis0 = self.frames[prev][drone]
            (x1, y1), vis1 = self.frames[turn][drone]
            if vis0 or vis1:
                result.append((drone, (x0 + (x1 - x0) * ratio,
                                       y0 + (y1 - y0) * ratio)))
        return result

    def count_in(self, zone: Optional[Zone], turn: int) -> int:
        """Return how many drones are in a zone at the end of a turn."""
        if zone is None:
            return 0
        return sum(1 for plan in self.plans
                   if self._step(plan, turn) == Step(zone.name))


class FlyInWindow:
    """Pygame window that animates the simulation.

    Controls: SPACE play/pause, LEFT/RIGHT previous/next turn,
    UP/DOWN speed, R restart, L labels, ESC or Q quit.
    """

    def __init__(self, graph: Graph, plans: List[Plan]) -> None:
        """Open the window and prepare everything to draw.

        Raises:
            pygame.error: If there is no display to open a window on.
        """
        pygame.display.init()
        headless = pygame.display.get_driver() in ("dummy", "offscreen")
        if headless and "SDL_VIDEODRIVER" not in os.environ:
            pygame.display.quit()
            raise pygame.error("no graphical display available")
        pygame.font.init()
        pygame.display.set_caption("Fly-in")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.SysFont("dejavusans,arial", 15)
        self.small = pygame.font.SysFont("dejavusans,arial", 12)
        self.bold = pygame.font.SysFont("dejavusans,arial", 18, bold=True)
        self.graph = graph
        self.layout = Layout(graph)
        self.timeline = Timeline(graph, plans, self.layout)
        self.simulation = Simulation(plans)
        self.time = 0.0
        self.speed = 1.0
        self.playing = True
        self.labels = True

    def run(self) -> None:
        """Run the main loop until the window is closed."""
        clock = pygame.time.Clock()
        running = True
        while running:
            delta = clock.tick(FPS) / 1000
            running = self._handle_events()
            if self.playing:
                self.time += delta * self.speed / TURN_SECONDS
                if self.time >= self.timeline.nb_turns:
                    self.time = float(self.timeline.nb_turns)
                    self.playing = False
            self.draw()
            pygame.display.flip()
        pygame.quit()

    def _handle_events(self) -> bool:
        """Apply keyboard input; return False when the user quits."""
        last = float(self.timeline.nb_turns)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key in (pygame.K_ESCAPE, pygame.K_q):
                return False
            if event.key == pygame.K_SPACE:
                if self.time >= last:
                    self.time = 0.0
                self.playing = not self.playing
            elif event.key == pygame.K_RIGHT:
                self.playing = False
                self.time = min(math.floor(self.time) + 1, last)
            elif event.key == pygame.K_LEFT:
                self.playing = False
                self.time = max(math.ceil(self.time) - 1, 0)
            elif event.key == pygame.K_r:
                self.time, self.playing = 0.0, True
            elif event.key == pygame.K_UP:
                self.speed = min(self.speed * 1.5, 8.0)
            elif event.key == pygame.K_DOWN:
                self.speed = max(self.speed / 1.5, 0.25)
            elif event.key == pygame.K_l:
                self.labels = not self.labels
        return True

    def draw(self) -> None:
        """Draw one frame: links, zones, drones and the HUD."""
        self.screen.fill(BACKGROUND)
        for link in self.graph.connections.values():
            a = self.layout.point(self.graph.zones[link.zone_a])
            b = self.layout.point(self.graph.zones[link.zone_b])
            width = 2 + link.max_link_capacity
            pygame.draw.line(self.screen, EDGE, a, b, width)
            if link.max_link_capacity > 1:
                mid = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2 - 12)
                self._text(f"x{link.max_link_capacity}", mid, self.small,
                           MUTED)
        turn = min(int(math.ceil(self.time)), self.timeline.nb_turns)
        for zone in self.graph.zones.values():
            self._draw_zone(zone, turn)
        if self.labels:
            for zone in self.graph.zones.values():
                self._draw_label(zone)
        for drone, pos in self.timeline.drones_at(self.time):
            self._draw_drone(drone, pos)
        self._draw_hud(turn)

    def _draw_zone(self, zone: Zone, turn: int) -> None:
        """Draw a zone circle with its type marks and label."""
        center = self.layout.point(zone)
        radius = self.layout.radius
        color = zone_color(zone)
        special = zone is self.graph.start or zone is self.graph.end
        if special:
            radius = int(radius * 1.3)
        pygame.draw.circle(self.screen, color, center, radius)
        if zone.zone_type is ZoneType.RESTRICTED:
            self._dashed_ring(center, radius + 5, (235, 80, 70))
        elif zone.zone_type is ZoneType.PRIORITY:
            pygame.draw.circle(self.screen, (120, 230, 255), center,
                               radius + 5, 3)
        elif zone.zone_type is ZoneType.BLOCKED:
            d = radius * 0.7
            x, y = center
            pygame.draw.line(self.screen, (20, 20, 20),
                             (x - d, y - d), (x + d, y + d), 4)
            pygame.draw.line(self.screen, (20, 20, 20),
                             (x - d, y + d), (x + d, y - d), 4)
        pygame.draw.circle(self.screen, (15, 15, 20), center, radius, 2)
        if special:
            count = self.timeline.count_in(zone, turn)
            self._text(str(count), center, self.bold, (15, 15, 20))

    def _draw_label(self, zone: Zone) -> None:
        """Write the zone name, alternating below/above by column.

        Neighbour columns get opposite sides so long names overlap less.
        """
        x, y = self.layout.point(zone)
        offset = self.layout.radius * 1.3 + 12
        side = 1 if zone.x % 2 == 0 else -1
        self._text(zone.name, (x, y + side * offset), self.small, TEXT)

    def _dashed_ring(self, center: Point, radius: int, color: RGB) -> None:
        """Draw a dashed circle (used for restricted zones)."""
        for i in range(0, 360, 30):
            start = math.radians(i)
            end = math.radians(i + 18)
            rect = pygame.Rect(0, 0, radius * 2, radius * 2)
            rect.center = (int(center[0]), int(center[1]))
            pygame.draw.arc(self.screen, color, rect, start, end, 3)

    def _draw_drone(self, drone: int, pos: Point) -> None:
        """Draw a drone as a small diamond with its number."""
        x, y = pos
        size = max(7, self.layout.radius // 3)
        points = [(x, y - size), (x + size, y), (x, y + size),
                  (x - size, y)]
        pygame.draw.polygon(self.screen, DRONE, points)
        pygame.draw.polygon(self.screen, (15, 15, 20), points, 2)
        self._text(str(drone), (x, y - size - 8), self.small, DRONE)

    def _draw_hud(self, turn: int) -> None:
        """Draw the turn counter, the current moves and the controls."""
        pygame.draw.rect(self.screen, (34, 37, 45), (0, 0, WIDTH, 56))
        total = len(self.timeline.plans)
        delivered = self.timeline.count_in(self.graph.end, turn)
        state = "playing" if self.playing else "paused"
        head = (f"Turn {turn}/{self.timeline.nb_turns}    "
                f"Delivered {delivered}/{total}    "
                f"Speed x{self.speed:.2f}    [{state}]")
        self._text(head, (16, 16), self.bold, TEXT, center=False)
        moves = " ".join(self.simulation.turn_moves(turn)) if turn else ""
        if len(moves) > 150:
            moves = moves[:147] + "..."
        self._text(moves, (16, 38), self.small, MUTED, center=False)
        help_text = ("SPACE play/pause   ←/→ turn   "
                     "↑/↓ speed   R restart   L labels   Q quit")
        self._text(help_text, (16, HEIGHT - 24), self.small, MUTED,
                   center=False)

    def _text(self, text: str, pos: Point, font: pygame.font.Font,
              color: RGB, center: bool = True) -> None:
        """Blit text centered on pos, or with its top-left at pos."""
        surface = font.render(text, True, color)
        rect = surface.get_rect()
        if center:
            rect.center = (int(pos[0]), int(pos[1]))
        else:
            rect.topleft = (int(pos[0]), int(pos[1]))
        self.screen.blit(surface, rect)
