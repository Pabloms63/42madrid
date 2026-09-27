from typing import Dict, Tuple
from fly_in.connection import Connection
from fly_in.graph import Graph
from fly_in.zone import Zone, ZoneType


ZONE_PREFIXES = ("start_hub", "end_hub", "hub")
ZONE_KEYS = ("zone", "color", "max_drones")
CONNECTION_KEYS = ("max_link_capacity",)


class ParseError(Exception):
    """Error raised when the map file is invalid."""

    def __init__(self, line_no: int, message: str) -> None:
        """Store the line number and the cause of the error."""
        super().__init__(f"line {line_no}: {message}")
        self.line_no = line_no
        self.message = message


class MapParser:
    """Read a map file and build a Graph."""

    def __init__(self) -> None:
        """Initialize the parser state."""

        self.graph = Graph()
        self.nb_drones = 0

    def parse(self, path: str) -> Tuple[Graph, int]:
        """Parse a map file.
        Args:
            path: Path to the map file.
        Returns:
            The built graph and the number of drones.
        Raises:
            ParseError: If the file content is invalid.
            OSError: If the file cannot be read."""

        line_no = 0
        with open(path, "rb") as file:
            for line_no, raw in enumerate(file, start=1):
                try:
                    text = raw.decode("utf-8")
                except UnicodeDecodeError:
                    raise ParseError(line_no, "invalid UTF-8 text") from None
                line = text.split("#", 1)[0].strip()
                if not line:
                    continue
                if self.nb_drones == 0:
                    self._parse_nb_drones(line, line_no)
                else:
                    self._dispatch(line, line_no)
        self._validate_final(line_no)
        return self.graph, self.nb_drones

    def _dispatch(self, line: str, line_no: int) -> None:
        """Send a line to the right handler depending on its prefix."""

        prefix, sep, rest = line.partition(":")
        prefix = prefix.strip()
        if not sep:
            raise ParseError(line_no, "missing ':' after the line type")
        if prefix in ZONE_PREFIXES:
            self._parse_zone(prefix, rest, line_no)
        elif prefix == "connection":
            self._parse_connection(rest, line_no)
        else:
            raise ParseError(line_no, f"unknown line type '{prefix}'")

    def _parse_nb_drones(self, line: str, line_no: int) -> None:
        """Parse the first line: 'nb_drones: <positive integer>'."""

        prefix, sep, value = line.partition(":")
        if not sep or prefix.strip() != "nb_drones":
            raise ParseError(
                line_no, "first line must be 'nb_drones: <number>'")
        self.nb_drones = self._to_int(value.strip(), "nb_drones", line_no,
                                      positive=True)

    def _parse_zone(self, prefix: str, rest: str, line_no: int) -> None:
        """Parse '<name> <x> <y> [metadata]' and add the zone.
        max_drones is ignored on start_hub/end_hub: they hold every drone."""

        main, meta = self._split_metadata(rest, ZONE_KEYS, line_no)
        parts = main.split()
        if len(parts) != 3:
            raise ParseError(line_no, "expected '<name> <x> <y> [metadata]'")
        name, raw_x, raw_y = parts
        if "-" in name:
            raise ParseError(line_no, f"zone name '{name}' contains '-'")
        try:
            zone_type = ZoneType(meta.get("zone", "normal"))
        except ValueError:
            raise ParseError(
                line_no, f"invalid zone type '{meta['zone']}'") from None

        is_hub = prefix == "hub"
        if not is_hub and zone_type is ZoneType.BLOCKED:
            raise ParseError(line_no, f"{prefix} cannot be blocked")
        if (prefix == "start_hub" and self.graph.start is not None
                or prefix == "end_hub" and self.graph.end is not None):
            raise ParseError(line_no, f"{prefix} defined more than once")

        zone = Zone(
            name=name,
            x=self._to_int(raw_x, "x coordinate", line_no),
            y=self._to_int(raw_y, "y coordinate", line_no),
            zone_type=zone_type,
            color=meta.get("color"),
            max_drones=self._to_int(meta.get("max_drones", "1"),
                                    "max_drones", line_no, positive=True)
            if is_hub else self.nb_drones,
        )
        try:
            self.graph.add_zone(zone)
        except ValueError as err:
            raise ParseError(line_no, str(err)) from None
        if prefix == "start_hub":
            self.graph.start = zone
        elif prefix == "end_hub":
            self.graph.end = zone

    def _parse_connection(self, rest: str, line_no: int) -> None:
        """Parse '<zone1>-<zone2> [metadata]' and add the connection."""

        main, meta = self._split_metadata(rest, CONNECTION_KEYS, line_no)
        names = main.split("-")
        if len(main.split()) != 1 or len(names) != 2 or not all(names):
            raise ParseError(
                line_no, f"expected '<zone1>-<zone2>', got '{main}'")
        capacity = self._to_int(meta.get("max_link_capacity", "1"),
                                "max_link_capacity", line_no, positive=True)
        try:
            self.graph.add_connection(
                Connection(names[0], names[1], capacity))
        except ValueError as err:
            raise ParseError(line_no, str(err)) from None

    @staticmethod
    def _split_metadata(
            rest: str, allowed: Tuple[str, ...], line_no: int
    ) -> Tuple[str, Dict[str, str]]:
        """Split 'text [k=v ...]' into the text and a metadata dict.
        Args:
            rest: The text after the ':' of the line.
            allowed: Metadata keys accepted for this kind of line.
            line_no: Line number in the file, for error messages.
        Returns:
            The text before '[' and the metadata ({} if there is none).
        Raises:
            ParseError: If the brackets or a tag are invalid, or a key
                is duplicated or not allowed."""

        main, bracket, block = rest.partition("[")
        if "]" in main:
            raise ParseError(line_no, "']' without matching '['")
        meta: Dict[str, str] = {}
        if not bracket:
            return main.strip(), meta
        block = block.strip()
        if not block.endswith("]") or "[" in block or "]" in block[:-1]:
            raise ParseError(line_no, f"invalid metadata block '[{block}'")
        for tag in block[:-1].split():
            key, sep, value = tag.partition("=")
            if not sep or not key or not value or "=" in value:
                raise ParseError(
                    line_no, f"invalid tag '{tag}', expected key=value")
            if key in meta:
                raise ParseError(line_no, f"duplicate metadata key '{key}'")
            if key not in allowed:
                raise ParseError(line_no, f"unknown metadata '{key}'")
            meta[key] = value
        return main.strip(), meta

    @staticmethod
    def _to_int(raw: str, what: str, line_no: int,
                positive: bool = False) -> int:
        """Convert text to int, raising ParseError if it is not valid.
        Only plain ASCII digits with an optional leading '-' are
        accepted ('1.5', '1_0' or '²' are rejected).
        Args:
            raw: The text to convert.
            what: Name of the value, used in the error message.
            line_no: Line number in the file, for error messages.
            positive: If True, the value must also be greater than 0.
        Returns:
            The integer value."""

        digits = raw[1:] if raw.startswith("-") else raw
        if not (digits.isascii() and digits.isdigit()):
            raise ParseError(
                line_no, f"{what} must be an integer, got '{raw}'")
        value = int(raw)
        if positive and value <= 0:
            raise ParseError(
                line_no, f"{what} must be a positive integer, got '{raw}'")
        return value

    def _validate_final(self, line_no: int) -> None:
        """Check that nb_drones, start_hub and end_hub were found."""

        if self.nb_drones == 0:
            raise ParseError(line_no, "empty file: missing 'nb_drones'")
        if self.graph.start is None:
            raise ParseError(line_no, "missing start_hub")
        if self.graph.end is None:
            raise ParseError(line_no, "missing end_hub")
