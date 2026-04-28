from .capability import TransformCapability
from ex0.base import Creature, CreatureFactory

class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str):
        TransformCapability.__init__(self)
        Creature.__init__(name, "Normal")
    
    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} shifts into a sharper form!"
    
    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} returns to normal"
    
    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally"


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str):
            TransformCapability.__init__(self)
            Creature().__init__(name, "Normal/Dragon")
