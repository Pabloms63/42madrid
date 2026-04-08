from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
            self, name: str, cost: int, rarity: str, 
            damage: int, combat_type: str,
            health: int, defense: int, mana: int
            ):
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.combat_type = combat_type
        self.health = health
        self.defense = defense
        self.mana = mana

    # Heredada por Card
    def play(self, game_stats: dict) -> dict:
        return {
            "card_played": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }
    
    # Heredada por Combatable
    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.damage,
            "combat_type": self.combat_type
        }

    # Heredada por Combatable
    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = min(self.defense, incoming_damage)
        damage_taken = max(0, incoming_damage - self.defense)

        self.health -= damage_taken

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > 0
        }
    
    # Heredada por Combatable
    def get_combat_stats(self) -> dict:
        return {
            "damage": self.damage,
            "health": self.health,
            "defense": self.defense,
            "combat_type": self.combat_type
        }

    # Heredada por Magical
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        spell_cost = 4  # coste fijo simple

        if self.mana < spell_cost:
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": targets,
                "error": "Not enough mana"
            }

        self.mana -= spell_cost

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": spell_cost
        }

    # Heredada por Magical
    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }
    
    # Heredada por Magical
    def get_magic_stats(self) -> dict:
        return {
            "mana": self.mana
        }
