from dataclasses import dataclass
from enum import Enum
from typing import Optional


class ZoneType(Enum):
	"""Possible types of a zone."""

	NORMAL = "normal"
	BLOCKED = "blocked"
	RESTRICTED = "restricted"
	PRIORITY = "priority"


@dataclass
class Zone:
	"""A node of the graph where drones can be.
	Attributes:
		name: Unique zone name (no dashes, no spaces).
		x: X coordinate.
		y: Y coordinate.
		zone_type: Type of the zone.
		color: Optional color used for display.
		max_drones: Maximum drones allowed at the same time."""

	name: str
	x: int
	y: int
	zone_types: ZoneType = ZoneType.NORMAL
	color: Optional[str] = None
	max_drones: int = 1

	@property
	def move_cost(self) -> int:
		"""Return the number of turns needed to enter this zone."""

		return 2 if self.zone_type is ZoneType.RESTRICTED else 1

	@property
	def is_accesible(self) -> bool:
		"""Return True if drones are allowed to enter this zone."""

		return self.zone_types is not ZoneType.BLOCKED
