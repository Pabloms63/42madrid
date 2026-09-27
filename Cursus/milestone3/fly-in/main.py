import sys
from fly_in.parser import MapParser, ParseError


USAGE = "usage: python3 main.py <map_file>"


def main() -> int:
    """Parse the map given as argument and run the program.

    Returns:
        The exit status: 0 on success, 1 on any error.
    """
    if len(sys.argv) != 2:
        print(USAGE, file=sys.stderr)
        return 1
    path = sys.argv[1]
    try:
        graph, nb_drones = MapParser().parse(path)
    except ParseError as err:
        print(f"Error: {path}: {err}", file=sys.stderr)
        return 1
    except OSError as err:
        print(f"Error: cannot read '{path}': {err.strerror}", file=sys.stderr)
        return 1

    # TODO: replace this summary with the simulation.
    assert graph.start is not None and graph.end is not None
    print(f"{nb_drones} drones: {graph.start.name} -> {graph.end.name}")
    print(f"{len(graph.zones)} zones, {len(graph.connections)} connections")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        sys.exit(130)
