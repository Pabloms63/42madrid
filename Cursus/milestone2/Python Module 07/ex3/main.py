from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    print("\n=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    print(f"Factory: {factory.__class__.__name__}")
    strategy = AggressiveStrategy()
    print(f"Strategy: {strategy.__class__.__name__}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\n Simulating aggressive turn...")
    deck = factory.create_themed_deck(3)
    hand = deck["cards"]
    battlefield = []
    print(f"Hand: {hand}")

    print("\nTurn execution:")
    print(f"Strategy: {strategy.__class__.__name__}")
    print(f"Actions: {strategy.execute_turn(hand, battlefield)}")

    print("\nGame Report:")
    engine = GameEngine()
    engine.configure_engine(factory, strategy)
    engine.simulate_turn()
    print(engine.get_engine_status())

    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
