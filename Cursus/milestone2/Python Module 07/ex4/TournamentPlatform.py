from ex4.TournamentCard import TournamentCard
from operator import attrgetter


class TournamentPlatform():
    def __init__(self):
        self.cards = {}
        self.matches_count = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards.update({card.card_id: card})
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        result1 = card1.attack(card2)
        result2 = card2.attack(card1)

        damage1 = result1["damage"]
        damage2 = result2["damage"]

        if damage1 > damage2:
            winner = card1
            loser = card2
        else:
            winner = card2
            loser = card1

        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_count += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        return sorted(self.cards.values(), key=attrgetter("rating"), reverse=True)

    def generate_tournament_report(self) -> dict:
        avg_rating = sum(card.rating for card in self.cards.values()) / len(self.cards)
        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_count,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
