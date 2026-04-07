from Card import Card
from typing import Dict, Any


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)

        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive numbers")

        self.attack = attack
        self.health = health

    def play(self) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }
    
    def attack_target(self, target: Any) -> Dict:
        target_name = getattr(target, "name", str(target))

        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }

    def get_card_info(self):
        info = super().get_card_info()

        info.update({
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        })
        return info
