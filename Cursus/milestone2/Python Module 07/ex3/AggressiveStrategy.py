from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        targets_attacked = ["Enemy Player"]

        for card in hand:
            power = 0

            if hasattr(card, "power"):
                power = card.power

            # Jugar cartas "baratas"
            if power <= 3:
                cards_played.append(str(card))
                mana_used += power
                damage_dealt += power

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        # Simple: poner primero al jugador si existe
        result = []

        if "Enemy Player" in available_targets:
            result.append("Enemy Player")

        for target in available_targets:
            if target != "Enemy Player":
                result.append(target)

        return result
