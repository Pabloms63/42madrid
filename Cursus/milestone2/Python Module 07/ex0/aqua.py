from .base import Creature, CreatureFactory


class Aquabub(Creature):
    def __init__(self, name: str):
        super().__init__(name, "Water")

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self, name: str):
        super().__init__(name, "Water")

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"


class AquaFactory(CreatureFactory):
    def create_base(self, name: str) -> Creature:
        return Aquabub(name)

    def create_evolved(self, name: str) -> Creature:
        return Torragon(name)
