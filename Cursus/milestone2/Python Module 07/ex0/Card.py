from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost

        try:
            self.rarity = Rarity(rarity)
        except ValueError:
            raise ValueError(f"Invalid rarity: {rarity}")

    @abstractmethod
    def play(self, game_state: Dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.value
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
