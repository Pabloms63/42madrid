from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard


def main():
    print("\n=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    deck = Deck()
    spell = SpellCard("Lightning Bolt", 3, "Common", "Deal 3 damage to target")
    artifact = ArtifactCard(
        "Mana Crystal", 2, "Common", 50, "Permanent: +1 mana per turn"
        )
    creature = CreatureCard("Vermithor", 5, "Legendary", 250, 5000)
    cards = [spell, artifact, creature]
    for card in cards:
        deck.add_card(card)
    deck_stats = deck.get_deck_stats()
    print(f"Deck stats: {deck_stats}")

    print(f"\nDrew: {spell.name} (Spell)")
    print(f"Play result: {spell.play({})}")

    print(f"\nDrew: {artifact.name} (Artifact)")
    print(f"Play result: {artifact.play({})}")

    print(f"\nDrew: {creature.name} (Creature)")
    print(f"Play result: {creature.play({})}")

    print("\nPolymorphism in action: Same interface, "
          "different card behaviors!")


if __name__ == "__main__":
    main()
