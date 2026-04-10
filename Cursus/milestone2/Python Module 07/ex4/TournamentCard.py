from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
import random


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, card_id: str):
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.wins = 0
        self.losses = 0
        self.rating = 1200

    def play(self, game_stats: dict) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def attack(self, target: "TournamentCard") -> dict:
        return {
            "attacker": self.card_id,
            "target": target.card_id,
            "damage": random.randint(1, self.cost)
        }

    def defend(self, incoming_damage: int):
        pass

    def get_combat_stats(self):
        pass

    def calculate_rating(self) -> int:
        return self.rating

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "rating": self.rating,
            "record": f"({self.wins}-{self.losses})"
        }

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        points = 16 * losses
        self.rating -= points

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        points = 16 * wins
        self.rating += points

    def get_rank_info(self):
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }
