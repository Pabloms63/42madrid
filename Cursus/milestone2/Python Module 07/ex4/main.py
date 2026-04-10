from ex0.Card import Card
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("\n=== DataDeck Tournament Platform ===\n")

    print("\nRegistering Tournament Cards...\n")

    dragon = TournamentCard("Fire Dragon", 15, "Epic", "dragon_001")
    print(f"{dragon.name} (ID: {dragon.card_id}):")
    interfaces = [base.__name__ for base in dragon.__class__.__bases__]
    print(f"- Interfaces: {interfaces}")
    print(f"- Rating: {dragon.rating}")
    print(f'- Record: {dragon.get_tournament_stats()["record"]}')

    wizard = TournamentCard("Ice Wizard", 10, "Rare", "wizard_001")
    print(f"\n{wizard.name} (ID: {wizard.card_id}):")
    interfaces = [base.__name__ for base in wizard.__class__.__bases__]
    print(f"- Interfaces: {interfaces}")
    print(f"- Rating: {wizard.rating}")
    print(f"- Record: {wizard.get_tournament_stats()['record']}")

    print("\nCreating tournament match...")
    platform = TournamentPlatform()
    platform.register_card(dragon)
    platform.register_card(wizard)
    result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {result}")

    print("\nTournament Leaderboard:")
    for i, card in enumerate(platform.get_leaderboard(), start=1):
        print(f"{i}. {card.name} - Rating: {card.rating} ({card.wins}-{card.losses})")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")

if __name__ == "__main__":
    main()
