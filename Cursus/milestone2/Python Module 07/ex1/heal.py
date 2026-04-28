from .capability import HealCapability
from ex0.base import Creature, CreatureFactory


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str):
        super().__init__(name, "Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: str | None = None) -> str:
        return f"{self.name} heals itlself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str):
        super().__init__(name, "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: str | None = None) -> str:
        return f"{self.name} heals itself and others for a large amount"


class HealingCreatureFactory(CreatureFactory):
    def create_base(self, name: str) -> Creature:
        return Sproutling(name)

    def create_evolved(self, name: str) -> Creature:
        return Bloomelle(name)
