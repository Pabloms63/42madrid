from .base import Creature, CreatureFactory


class Flameling(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class FlameFactory(CreatureFactory):
    def create_base(self, name: str) -> Creature:
        return Flameling(name)

    def create_evolved(self, name: str) -> Creature:
        return Pyrodon(name)
