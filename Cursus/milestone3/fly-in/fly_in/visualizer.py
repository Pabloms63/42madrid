import os
import sys
from typing import Dict, List, Optional
from fly_in.graph import Graph
from fly_in.planner import Plan, Step
from fly_in.simulation import Simulation


ANSI_CODES: Dict[str, int] = {
    "red": 196, "green": 46, "blue": 33, "yellow": 226, "orange": 208,
    "cyan": 51, "purple": 129, "magenta": 201, "pink": 213,
    "gray": 245, "grey": 245, "black": 240, "white": 255, "brown": 130,
    "gold": 220, "lime": 118, "maroon": 88, "darkred": 124,
    "crimson": 161, "violet": 177,
}
RAINBOW = (196, 208, 226, 46, 33, 129)
RESET = "\033[0m"


class Painter:
    """Wrap text in ANSI colors, or leave it plain when colors are off."""

    def __init__(self, enabled: Optional[bool] = None) -> None:
        """Enable colors only on a real terminal, unless forced.

        The NO_COLOR environment variable always disables them.
        """
        if enabled is None:
            enabled = sys.stdout.isatty()
        self.enabled = enabled and "NO_COLOR" not in os.environ

    def color(self, text: str, color: Optional[str]) -> str:
        """Paint text with a map color name (unknown names stay plain)."""
        if not self.enabled or color is None:
            return text
        name = color.lower()
        if name == "rainbow":
            return "".join(self._code(ch, RAINBOW[i % len(RAINBOW)])
                           for i, ch in enumerate(text)) + RESET
        code = ANSI_CODES.get(name)
        return text if code is None else self._code(text, code) + RESET

    def style(self, text: str, sgr: str) -> str:
        """Apply a raw SGR style such as '1' (bold) or '2' (dim)."""
        return f"\033[{sgr}m{text}{RESET}" if self.enabled else text

    @staticmethod
    def _code(text: str, code: int) -> str:
        """Return text prefixed with a 256-color foreground code."""
        return f"\033[38;5;{code}m{text}"


class Visualizer:
    """Print the simulation with colors, zone states and statistics."""

    def __init__(self, graph: Graph, plans: List[Plan],
                 painter: Optional[Painter] = None) -> None:
        """Store what is needed to draw every turn."""
        self.graph = graph
        self.plans = plans
        self.simulation = Simulation(plans)
        self.paint = painter if painter is not None else Painter()

    def colored_output(self) -> List[str]:
        """Return the standard output lines, each move in its zone color."""
        lines: List[str] = []
        for turn in range(1, self.simulation.nb_turns + 1):
            moves = [self._paint_move(move)
                     for move in self.simulation.turn_moves(turn)]
            lines.append(" ".join(moves))
        return lines

    def report(self) -> List[str]:
        """Return the detailed view: legend, turns with states, stats."""
        lines = [self.paint.style("Zones:", "1"), self._legend(), ""]
        output = self.colored_output()
        for turn, moves in enumerate(output, start=1):
            header = self.paint.style(f"Turn {turn:>3}", "1")
            lines.append(f"{header}  {moves}")
            lines.append(f"          {self._state(turn)}")
        lines.append("")
        lines.extend(self._stats())
        return lines

    def _paint_move(self, move: str) -> str:
        """Color 'D1-zone' (or 'D1-a-b' in transit) by its destination."""
        drone, _, where = move.partition("-")
        zone = self.graph.zones.get(where)
        if zone is None:
            return self.paint.style(move, "3")
        return f"{drone}-{self.paint.color(where, zone.color)}"

    def _legend(self) -> str:
        """Return every zone with its color, type and capacity."""
        parts: List[str] = []
        for zone in self.graph.zones.values():
            label = self.paint.color(zone.name, zone.color)
            info = zone.zone_type.value
            if zone is not self.graph.start and zone is not self.graph.end:
                info += f", max {zone.max_drones}"
            parts.append(f"{label} ({info})")
        return "  " + "  ".join(parts)

    def _state(self, turn: int) -> str:
        """Return where every drone is at the end of a turn."""
        start = self.graph.start
        end = self.graph.end
        assert start is not None and end is not None
        occupants: Dict[str, List[int]] = {}
        in_flight: List[str] = []
        for drone_id, plan in enumerate(self.plans, start=1):
            step: Step = plan[min(turn, len(plan) - 1)]
            if step.link is not None:
                in_flight.append(f"D{drone_id}->{step.zone}")
            else:
                occupants.setdefault(step.zone, []).append(drone_id)
        parts = [f"{start.name}: {len(occupants.pop(start.name, []))}"]
        delivered = len(occupants.pop(end.name, []))
        for name, drones in occupants.items():
            zone = self.graph.zones[name]
            fill = f"{len(drones)}/{zone.max_drones}"
            if len(drones) >= zone.max_drones:
                fill = self.paint.style(fill, "1")
            ids = ",".join(f"D{d}" for d in drones)
            parts.append(f"{self.paint.color(name, zone.color)}"
                         f"[{ids}] {fill}")
        if in_flight:
            parts.append(self.paint.style(
                "flying: " + " ".join(in_flight), "3"))
        parts.append(f"{end.name}: {delivered}/{len(self.plans)}")
        return self.paint.style(" | ", "2").join(parts)

    def _stats(self) -> List[str]:
        """Return the main and secondary metrics of the subject."""
        turns = self.simulation.nb_turns
        arrivals = [len(plan) - 1 for plan in self.plans]
        moves = [len(self.simulation.turn_moves(t))
                 for t in range(1, turns + 1)]
        average = sum(arrivals) / len(arrivals) if arrivals else 0.0
        per_turn = sum(moves) / turns if turns else 0.0
        return [
            self.paint.style("Summary:", "1"),
            f"  total turns          : {self.paint.style(str(turns), '1')}",
            f"  drones delivered     : {len(self.plans)}",
            f"  avg turns per drone  : {average:.2f}",
            f"  avg moves per turn   : {per_turn:.2f}",
        ]
