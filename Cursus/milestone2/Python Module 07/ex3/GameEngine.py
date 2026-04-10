from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.hand = []
        self.battlefield = []
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(
            self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

        deck = self.factory.create_themed_deck(3)
        self.hand = deck["cards"]
        self.cards_created = len(self.hand)

    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            return {}

        result = self.strategy.execute_turn(self.hand, self.battlefield)

        self.turns_simulated += 1
        self.total_damage += result.get("damage_dealt", 0)

        return result

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name()
            if self.strategy else None,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
