from typing import Dict, FrozenSet, List, Optional
from fly_in.connection import Connection
from fly_in.zone import Zone


class Graph:
    """Network of zones linked by connections."""

    def __init__(self) -> None:
        """Create an empty graph"""

        self.zones: Dict[str, Zone] = {}
        self.connections: Dict[FrozenSet[str], Connection] = {}
        self.adjacency: Dict[str, List[Connection]] = {}
        self.start: Optional[Zone] = None
        self.end: Optional[Zone] = None

    def add_zone(self, zone: Zone) -> None:
        """Add a zone to the graph.
        Raises:
            ValueError: If a zone with the same name already exists."""

        if zone.name in self.zones:
            raise ValueError(f"duplicate zone '{zone.name}'")
        self.zones[zone.name] = zone
        self.adjacency[zone.name] = []

    def add_connection(self, connection: Connection) -> None:
        """Add a bidirectional connection
        Raises:
            ValueError: If a zone is unknown or the connection exists."""

        for name in (connection.zone_a, connection.zone_b):
            if name not in self.zones:
                raise ValueError(f"unknown zone '{name}")
        if connection.zone_a == connection.zone_b:
            raise ValueError("a zone cannot be connected to itself")
        if connection.key in self.connections:
            raise ValueError(f"duplicate connection '{connection.name}'")
        self.connections[connection.key] = connection
        self.adjacency[connection.zone_a].append(connection)
        self.adjacency[connection.zone_b].append(connection)

    def neigbors(self, zone_name: str) -> List[Connection]:
        """Return the connections leaving a zone."""

        return self.adjacency.get(zone_name, [])

    def get_connection(self, a: str, b: str) -> Optional[Connection]:
        """Return the connection between two zones, if any."""

        return self.connections.get(frozenset((a, b)))
