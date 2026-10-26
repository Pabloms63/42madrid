*This project has been created as part of the 42 curriculum by <pmarcos->.*

# Fly-in

## Description

Fly-in routes a fleet of drones from a start zone to an end zone through a
network of connected zones, in the **fewest possible simulation turns**.

The map is a graph: zones (nodes) linked by bidirectional connections
(edges). Zones have a type (`normal`, `restricted`, `priority`, `blocked`)
and a capacity (`max_drones`); connections have a capacity
(`max_link_capacity`). Every turn, each drone may move to a neighbour zone,
fly toward a restricted zone (2 turns), or wait. The program must respect
every capacity at every turn, avoid conflicts and deadlocks, and print the
moves of each turn.

The project contains:

- a **parser** that validates the map file and reports any error with its
  line number and cause;
- a **multi-agent pathfinding** algorithm that plans every drone's route in
  space and time;
- a **simulation** that prints the turn-by-turn output in the required format;
- two **visual representations**: colored terminal output and an animated
  graphical window (pygame).

No graph library is used: all graph logic is written from scratch.

## Instructions

Requirements: Python 3.10 or later.

```bash
python3 -m venv .venv && source .venv/bin/activate
make install                      # flake8, mypy, pygame
```

| Command | What it does |
|---|---|
| `make run MAP=<file>` | Print the simulation (colored when printed to a terminal) |
| `make visual MAP=<file>` | Detailed terminal view: legend, zone states per turn, summary |
| `make gui MAP=<file>` | Print the simulation, then open the animated window |
| `make debug MAP=<file>` | Run the program under `pdb` |
| `make lint` / `make lint-strict` | Run flake8 and mypy (normal / `--strict`) |
| `make clean` | Remove `__pycache__` and `.mypy_cache` |

`MAP` defaults to `maps/easy/01_linear_path.txt`. The program can also be run directly:

```bash
python3 main.py [--visual] [--gui] <map_file>
```

Window controls: `SPACE` play/pause, `←/→` previous/next turn, `↑/↓` speed,
`R` restart, `L` show/hide zone names, `Q` or `ESC` quit.

## Algorithm

### Approach: prioritized planning with a reservation table

Finding one shortest path is easy; moving many drones at once without
collisions is the real problem. The planner therefore searches in a
**time-expanded graph** whose states are `(zone, turn)`. From state
`(A, t)` a drone can:

- **wait**: go to `(A, t+1)`, if `A` still has room at `t+1`;
- **move** to a normal or priority neighbour `B`: go to `(B, t+1)`;
- **fly** to a restricted neighbour `R`: it is on the connection during
  turn `t+1` and lands in `(R, t+2)`. It cannot stop halfway;
- never enter a `blocked` zone.

Drones are planned **one after another**. A `ReservationTable` stores, for
every turn, how many drones are in each zone and on each connection. Each
drone looks for its earliest arrival using only the capacity left by the
drones planned before it, then reserves its own path. `start_hub` and
`end_hub` have unlimited capacity.

The search processes turns in increasing order (a dynamic programme over
time layers), so the first turn in which the end zone is reached is the
earliest possible arrival for that drone. Equal arrivals are broken by:

1. visiting **more priority zones** (the subject says they should be
   preferred);
2. leaving the start **as late as possible**, so a drone waits where
   capacity is unlimited instead of blocking a narrow zone.

### Why it meets the requirements

| Requirement | How |
|---|---|
| Distribution across paths | When the short path is full, the next drone arrives earlier through another one and takes it |
| Strategic waiting | Waiting is just another move, chosen when it pays off |
| No conflicts or deadlocks | Each drone only uses capacity that is still free, so two drones never compete for the same slot |
| Zone and link capacities | Checked against the reservation table for every turn |
| Freed capacity in the same turn | Occupancy is counted at the end of each turn, so a drone can enter a zone another drone just left |
| Restricted zones | Two-turn move that occupies the connection during transit |

Before planning, a breadth-first search checks that the end zone is
reachable at all; if not, the program stops with a clear error instead of
searching forever.

### Complexity

Per drone, the search visits at most `T × V` states and tries each
connection, with `T` the turn horizon, `V` the zones and `E` the
connections: `O(T · (V + E))`. For `D` drones: `O(D · T · (V + E))`.
Paths are not cached between drones because each one depends on the
reservations of the previous ones; memory is `O(T · (V + E))` for the
reservation table. All provided maps are solved in less than 0.2 seconds.

### Limitation

Planning drones one by one is not guaranteed to find the global optimum
(the order of the drones matters), but every plan is valid by
construction and the results beat every reference target below.

### Results on the provided maps

Every result was checked with an independent validator that replays the
output and verifies all the movement and capacity rules.

| Map | Drones | Turns | Target |
|---|---|---|---|
| easy / linear_path | 2 | **4** | ≤ 6 |
| easy / simple_fork | 4 | **4** | ≤ 8 |
| easy / basic_capacity | 4 | **4** | ≤ 6 |
| medium / dead_end_trap | 5 | **8** | ≤ 12 |
| medium / circular_loop | 6 | **15** | ≤ 15 |
| medium / priority_puzzle | 5 | **7** | ≤ 12 |
| hard / maze_nightmare | 8 | **13** | ≤ 30 |
| hard / capacity_hell | 12 | **16** | ≤ 35 |
| hard / ultimate_challenge | 15 | **26** | ≤ 45 |
| challenger / the_impossible_dream | 25 | **43** | record: 45 |

`circular_loop` cannot go below 15: its only exit is a restricted zone with
capacity 1, so one drone gets through every 2 turns.

### Parser

The parser checks the file at three levels and stops at the first error,
printing `line N: <cause>`:

1. **Line**: known prefix, `:` present, correct number of fields, integer
   coordinates, zone names without dashes or spaces.
2. **Metadata** `[k=v ...]`: brackets, `key=value` syntax, no duplicate
   keys, only the keys allowed for that line, valid zone type, positive
   capacities.
3. **Whole file**: first line is `nb_drones`, exactly one start and one
   end, unique zone names, connections between already defined zones, no
   duplicate connections (`a-b` equals `b-a`).

As the subject requires, `max_drones` is ignored on `start_hub` and
`end_hub`.

## Visual representation

**Terminal** (`make run`, `make visual`): each move is printed in the color
of its destination zone (the `color=` of the map, as 256-color ANSI codes).
Drones flying toward a restricted zone are shown in italics. Colors are
only used when writing to a terminal, so redirected output is plain text in
the exact required format; `NO_COLOR` is also respected. The `--visual`
mode adds a legend of all zones, the state of every zone after each turn
(which drones are where, full zones in bold, drones in flight, delivered
count) and a summary with the secondary metrics of the subject.

**Graphical window** (`make gui`): the network is drawn from the map
coordinates. Zones use their map color; restricted zones have a dashed red
ring, priority zones a light blue ring and blocked zones a cross. Thicker
connections have more capacity. Drones are numbered diamonds that slide
smoothly between zones and stay halfway on the connection while flying to
a restricted zone. The header shows the turn, the delivered drones and the
moves of the current turn, and the simulation can be paused and stepped
turn by turn. This makes it easy to see where drones queue, how they split
between paths and why waiting is sometimes the best move.

## Example

Input (`maps/example.txt`):

```
nb_drones: 5

start_hub: hub 0 0 [color=green]
end_hub: goal 10 10 [color=yellow]
hub: roof1 3 4 [zone=restricted color=red]
hub: roof2 6 2 [zone=normal color=blue]
hub: corridorA 4 3 [zone=priority color=green max_drones=2]
hub: tunnelB 7 4 [zone=normal color=red]
hub: obstacleX 5 5 [zone=blocked color=gray]
connection: hub-roof1
connection: hub-corridorA
connection: roof1-roof2
connection: roof2-goal
connection: corridorA-tunnelB [max_link_capacity=2]
connection: tunnelB-goal
```

Output (`make run`):

```
D1-corridorA D3-hub-roof1
D1-tunnelB D2-corridorA D3-roof1
D1-goal D2-tunnelB D3-roof2 D4-corridorA
D2-goal D3-goal D4-tunnelB D5-corridorA
D4-goal D5-tunnelB
D5-goal
```

All 5 drones are delivered in **6 turns**. D3 takes the slower restricted
path (`hub-roof1` is the turn it spends on the connection), because it
reaches the goal sooner than waiting behind the others on the priority
path. Summary from `make visual`: average 4.40 turns per drone,
2.67 moves per turn.

## Project structure

```
main.py              entry point: arguments, error handling, output
fly_in/zone.py       Zone and ZoneType
fly_in/connection.py Connection (bidirectional edge)
fly_in/graph.py      Graph: zones, connections, adjacency
fly_in/parser.py     MapParser and ParseError
fly_in/planner.py    ReservationTable and Planner (pathfinding)
fly_in/simulation.py turn-by-turn output
fly_in/visualizer.py colored terminal output
fly_in/gui.py        pygame window
maps/                example and test maps
```

## Resources

- Silver, D. (2005). *Cooperative Pathfinding*. AIIDE. The origin of
  prioritized planning with a reservation table.
- Stern, R. et al. (2019). *Multi-Agent Pathfinding: Definitions,
  Variants, and Benchmarks*. SoCS.
- Dijkstra's algorithm and breadth-first search, *Introduction to
  Algorithms* (Cormen et al.), chapters on graph algorithms.
- [Python `typing`](https://docs.python.org/3/library/typing.html),
  [mypy](https://mypy.readthedocs.io/),
  [flake8](https://flake8.pycqa.org/).
- [pygame documentation](https://www.pygame.org/docs/).
- [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code)
  (256-color mode).

### Use of AI

An AI assistant (Claude) was used during this project for:

- **Code review**: finding bugs, type errors and style issues in the
  parser and the data model.
- **Implementation support**: drafting parts of the parser, the planner,
  the terminal visualizer and the pygame window, which were then reviewed,
  tested and adapted.
- **Testing**: writing an independent validator to check every output
  against the movement and capacity rules, and edge-case map files for the
  parser.
