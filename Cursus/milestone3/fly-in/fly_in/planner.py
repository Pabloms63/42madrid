from collections import deque
from dataclasses import dataclass
from typing import Dict, FrozenSet, List, Optional, Set, Tuple
from fly_in.connection import Connection
from fly_in.graph import Graph
from fly_in.zone import Zone, ZoneType


class PlanningError(Exception):
    """Error raised when the drones cannot reach the end zone."""


@dataclass(frozen=True)
class Step:
    """Position of a drone at the end of a turn.

    Attributes:
        zone: The zone the drone is in, or is flying to if in transit.
        link: The connection being crossed toward a restricted zone,
            or None when the drone is inside a zone.
    """

    zone: str
    link: Optional[Connection] = None


Plan = List[Step]
State = Tuple[str, int]
Score = Tuple[int, int]


class ReservationTable:
    """Count, turn by turn, how many drones use each zone and link."""

    def __init__(self, graph: Graph) -> None:
        """Create an empty table for the given graph."""
        self.graph = graph
        self.zones: Dict[State, int] = {}
        self.links: Dict[Tuple[FrozenSet[str], int], int] = {}
        self.last_turn = 0

    def zone_free(self, zone: Zone, turn: int) -> bool:
        """Return True if one more drone fits in the zone at that turn.

        start_hub and end_hub have no capacity limit.
        """
        if zone is self.graph.start or zone is self.graph.end:
            return True
        return self.zones.get((zone.name, turn), 0) < zone.max_drones

    def link_free(self, link: Connection, turn: int) -> bool:
        """Return True if one more drone can cross the link that turn."""
        used = self.links.get((link.key, turn), 0)
        return used < link.max_link_capacity

    def reserve(self, plan: Plan) -> None:
        """Mark every zone and link used by a plan as taken."""
        for turn, step in enumerate(plan):
            if step.link is None:
                key = (step.zone, turn)
                self.zones[key] = self.zones.get(key, 0) + 1
            if turn == 0:
                continue
            link = self._link_used(plan[turn - 1], step)
            if link is not None:
                key2 = (link.key, turn)
                self.links[key2] = self.links.get(key2, 0) + 1
        self.last_turn = max(self.last_turn, len(plan) - 1)

    def _link_used(self, prev: Step, step: Step) -> Optional[Connection]:
        """Return the link crossed between two consecutive steps."""
        if step.link is not None:
            return step.link
        if prev.link is not None:
            return prev.link
        if prev.zone != step.zone:
            return self.graph.get_connection(prev.zone, step.zone)
        return None


class Planner:
    """Plan the path of every drone, one after another.

    Each drone looks for the earliest arrival at the end zone in a
    (zone, turn) space, avoiding what earlier drones already reserved.
    Ties are broken by visiting more priority zones, then by leaving
    the start zone as late as possible (waiting where it is free).
    """

    def __init__(self, graph: Graph, nb_drones: int) -> None:
        """Prepare the planner.

        Raises:
            PlanningError: If the end zone cannot be reached at all.
        """
        if graph.start is None or graph.end is None:
            raise PlanningError("start and end zones are required")
        self.graph = graph
        self.start: Zone = graph.start
        self.end: Zone = graph.end
        self.nb_drones = nb_drones
        self.table = ReservationTable(graph)
        if not self._reachable():
            raise PlanningError(
                f"no path from '{self.start.name}' to '{self.end.name}'")

    def plan_all(self) -> List[Plan]:
        """Return one plan per drone (index 0 is drone D1)."""
        plans: List[Plan] = []
        for _ in range(self.nb_drones):
            plan = self._plan_one()
            self.table.reserve(plan)
            plans.append(plan)
        return plans

    def _plan_one(self) -> Plan:
        """Find the best plan for one drone given the reservations.

        Every turn is a layer; a move to a restricted zone jumps two
        layers ahead. Layers are processed in order, so the first
        layer that contains the end zone gives the earliest arrival.
        """
        horizon = self.table.last_turn + 2 * len(self.graph.zones) + 2
        layers: List[Dict[str, Tuple[Score, Optional[State]]]] = [
            {} for _ in range(horizon + 3)]
        layers[0][self.start.name] = ((0, 0), None)
        for turn in range(horizon + 1):
            if self.end.name in layers[turn]:
                return self._rebuild(layers, (self.end.name, turn))
            for name, (score, _) in list(layers[turn].items()):
                self._expand(layers, name, turn, score)
        raise PlanningError("no plan found within the turn limit")

    def _expand(self, layers: List[Dict[str, Tuple[Score, Optional[State]]]],
                name: str, turn: int, score: Score) -> None:
        """Add every state reachable from (name, turn) to the layers."""
        zone = self.graph.zones[name]
        prio, busy = score
        if zone is self.start:
            self._offer(layers, name, turn + 1, (prio, busy), (name, turn))
        elif self.table.zone_free(zone, turn + 1):
            self._offer(layers, name, turn + 1, (prio, busy + 1),
                        (name, turn))
        for link in self.graph.neigbors(name):
            target = self.graph.zones[link.other(name)]
            if not target.is_accesible or target is self.start:
                continue
            arrival = turn + target.move_cost
            if not self.table.zone_free(target, arrival):
                continue
            if not all(self.table.link_free(link, t)
                       for t in range(turn + 1, arrival + 1)):
                continue
            bonus = 1 if target.zone_type is ZoneType.PRIORITY else 0
            self._offer(layers, target.name, arrival,
                        (prio - bonus, busy + target.move_cost),
                        (name, turn))

    @staticmethod
    def _offer(layers: List[Dict[str, Tuple[Score, Optional[State]]]],
               name: str, turn: int, score: Score, parent: State) -> None:
        """Keep the state if it is new or better than the known one."""
        known = layers[turn].get(name)
        if known is None or score < known[0]:
            layers[turn][name] = (score, parent)

    def _rebuild(self, layers: List[Dict[str, Tuple[Score, Optional[State]]]],
                 state: State) -> Plan:
        """Follow the parents back to the start and build the plan."""
        plan: Plan = []
        current: Optional[State] = state
        while current is not None:
            name, turn = current
            parent = layers[turn][name][1]
            plan.append(Step(name))
            if parent is not None and turn - parent[1] == 2:
                link = self.graph.get_connection(parent[0], name)
                plan.append(Step(name, link))
            current = parent
        plan.reverse()
        return plan

    def _reachable(self) -> bool:
        """Return True if the end can be reached ignoring capacities."""
        seen: Set[str] = {self.start.name}
        queue = deque([self.start.name])
        while queue:
            name = queue.popleft()
            if name == self.end.name:
                return True
            for link in self.graph.neigbors(name):
                other = link.other(name)
                zone = self.graph.zones[other]
                if other not in seen and zone.is_accesible:
                    seen.add(other)
                    queue.append(other)
        return False
