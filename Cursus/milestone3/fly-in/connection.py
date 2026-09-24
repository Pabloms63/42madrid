from dataclasses import dataclass
from typing import FrozenSet


@dataclass
class Connection:
	"""A bidirectional edge between two zones.
	
	Attributes:
		zone_a: Name of the first zone.
		zone_b: Name of the second zone.
		max_link_capacity: Drones allowed on the link at the same time."""

	zone_a: str
	zone_b: str
	max_link_capacity: int = 1

	@property
	def key(self) -> FrozenSet[str]:
		"""Return an order-independent key (a-b == b-a)."""

		return frozenset((self.zone_a, self.zone_b))

	@property
	def name(self) -> str:
		"""Return the connection name used in the simulation output."""

		return f"{self.zone_a}-{self.zone_b}"

	def other(self, zone_name: str) -> str:
		"""Return the zone at the other end of the connection.
		Args:
			zone_name: One end of the connection.
		Returns:
			The name of the opposite end.
		Raises:
			ValueError: If zone_name is not part of this connection."""

		if zone_name == self.zone_a:
			return self.zone_b
		if zone_name == self.zone_b:
			return self.zone_a
		raise ValueError(f"{zone_name} is not part of {self.name}")