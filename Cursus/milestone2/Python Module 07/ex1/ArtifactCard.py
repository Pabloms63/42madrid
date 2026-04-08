from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
            self, name: str, cost: int, rarity: str,
            durability: int, effect: str
            ):
        super().__init__(name, cost, rarity)
        if durability <= 0:
            raise ValueError("Durability must be positive")

        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

    def activate_ability(self) -> dict:
        self.durability -= 1

        return {
            "artifact": self.name,
            "effect": self.effect,
            "remaining_durability": self.durability
        }
