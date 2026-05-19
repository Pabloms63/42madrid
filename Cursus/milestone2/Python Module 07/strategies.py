from typing import TypeGuard

from .base_strategy import BattleStrategy
from ex0.base import Creature
from ex1.transform import TransformCapability
from ex1.heal import HealCapability


class StrategyError(Exception):
    pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggresiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
            return
        raise StrategyError(
            f"Invalid Creature '{creature.__class__.__name__}'"
            f" for this aggressive strategy"
        )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if isinstance(creature, HealCapability):
            print(creature.attack())
            print(creature.heal())
            return
        raise StrategyError(
            f"Invalid Creature '{creature.__class__.__name__}'"
            f" for this defensive strategy"
        )