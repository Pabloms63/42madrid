from typing import List
from fly_in.planner import Plan


class Simulation:
    """Turn the drone plans into the turn-by-turn output."""

    def __init__(self, plans: List[Plan]) -> None:
        """Store the plans (index 0 is drone D1)."""
        self.plans = plans

    @property
    def nb_turns(self) -> int:
        """Return the number of turns needed to deliver every drone."""
        return max((len(plan) - 1 for plan in self.plans), default=0)

    def turn_moves(self, turn: int) -> List[str]:
        """Return the moves of one turn, like ['D1-roof1', 'D2-a-b'].

        Drones that wait, or that were already delivered, are omitted.
        """
        moves: List[str] = []
        for drone_id, plan in enumerate(self.plans, start=1):
            if turn >= len(plan):
                continue
            step, prev = plan[turn], plan[turn - 1]
            if step.link is not None:
                moves.append(f"D{drone_id}-{step.link.name}")
            elif step.zone != prev.zone or prev.link is not None:
                moves.append(f"D{drone_id}-{step.zone}")
        return moves

    def output(self) -> List[str]:
        """Return one line per turn, in the subject's format."""
        return [" ".join(self.turn_moves(turn))
                for turn in range(1, self.nb_turns + 1)]
