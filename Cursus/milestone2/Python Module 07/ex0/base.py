from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str):
        self.name = name
        self.creture_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.creture_type} type Creature"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self, name: str) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self, name: str) -> Creature:
        pass
