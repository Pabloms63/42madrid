import random
from ex3.CardFactory import CardFactory
from ex0.Card import Card


class SimpleCard(Card):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def play(self):
        return f"{self.name} is played"

    def __str__(self):
        return f"{self.name} ({self.power})"


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power=None) -> Card:
        names = ["Dragon", "Goblin", "Knight", "Orc"]
        name = name_or_power if isinstance(
            name_or_power, str) else random.choice(names)
        power = name_or_power if isinstance(
            name_or_power, int) else random.randint(1, 6)

        return SimpleCard(name, power)

    def create_spell(self, name_or_power=None) -> Card:
        names = ["Fireball", "Lightning", "Ice Blast"]
        name = name_or_power if isinstance(
            name_or_power, str) else random.choice(names)
        power = name_or_power if isinstance(
            name_or_power, int) else random.randint(2, 7)

        return SimpleCard(name, power)

    def create_artifact(self, name_or_power=None) -> Card:
        names = ["Mana Ring", "Crystal", "Staff"]
        name = name_or_power if isinstance(
            name_or_power, str) else random.choice(names)
        power = name_or_power if isinstance(
            name_or_power, int) else random.randint(1, 5)

        return SimpleCard(name, power)

    def create_themed_deck(self, size: int) -> dict:
        cards = []

        for _ in range(size):
            choice = random.choice(["creature", "spell", "artifact"])

            if choice == "creature":
                cards.append(self.create_creature())
            elif choice == "spell":
                cards.append(self.create_spell())
            else:
                cards.append(self.create_artifact())

        return {"cards": cards}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin", "knight", "orc"],
            "spells": ["fireball", "lightning", "ice blast"],
            "artifacts": ["mana ring", "crystal", "staff"]
        }
