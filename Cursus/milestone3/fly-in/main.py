import sys
from typing import List
from fly_in.graph import Graph
from fly_in.parser import MapParser, ParseError
from fly_in.planner import Plan, Planner, PlanningError
from fly_in.visualizer import Visualizer


USAGE = "usage: python3 main.py [--visual] [--gui] <map_file>"


def main() -> int:
    """Parse the map, plan every drone and print the simulation.

    With --visual, also print a legend, the zone states after every
    turn and a summary with the subject's metrics. With --gui, open
    an animated window after printing the output.

    Returns:
        The exit status: 0 on success, 1 on any error.
    """
    args = sys.argv[1:]
    visual = "--visual" in args
    gui = "--gui" in args
    args = [arg for arg in args if arg not in ("--visual", "--gui")]
    if len(args) != 1:
        print(USAGE, file=sys.stderr)
        return 1
    path = args[0]
    try:
        graph, nb_drones = MapParser().parse(path)
    except ParseError as err:
        print(f"Error: {path}: {err}", file=sys.stderr)
        return 1
    except OSError as err:
        print(f"Error: cannot read '{path}': {err.strerror}", file=sys.stderr)
        return 1

    try:
        plans = Planner(graph, nb_drones).plan_all()
    except PlanningError as err:
        print(f"Error: {path}: {err}", file=sys.stderr)
        return 1
    visualizer = Visualizer(graph, plans)
    lines = visualizer.report() if visual else visualizer.colored_output()
    for line in lines:
        print(line)
    return open_window(graph, plans) if gui else 0


def open_window(graph: Graph, plans: List[Plan]) -> int:
    """Show the pygame window; return 1 if it cannot be opened."""
    try:
        from fly_in.gui import FlyInWindow
        import pygame
    except ImportError:
        print("Error: pygame is not installed (run 'make install')",
              file=sys.stderr)
        return 1
    try:
        FlyInWindow(graph, plans).run()
    except pygame.error as err:
        print(f"Error: cannot open the window: {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        sys.exit(130)
