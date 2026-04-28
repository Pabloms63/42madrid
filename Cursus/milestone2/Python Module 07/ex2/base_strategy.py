from abc import ABC, abstractmethod
from ex0.base import Creature


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creture: Creature) -> None:
        pass
