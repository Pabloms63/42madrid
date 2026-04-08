from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard


def get_methods(cls) -> list:
    return [
        name for name, value in cls.__dict__.items()
        if callable(value) and not name.startswith("__")
    ]


def main():
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print(f"- Card: {get_methods(Card)}")
    print(f"- Combatable: {get_methods(Combatable)}")
    print(f"- Magical: {get_methods(Magical)}")

    elite = EliteCard("Arcane Warrior", 4, "Rare", 5, "melee", 20, 3, 8)
    print(f"Playing {elite.name} (Elite Card)")

    print("\nCombat phase:")
    print(f'Attack result: {elite.attack("Enemy")}')
    print(f'Defense result: {elite.defend(5)}')

    print("\nMagic phase: ")
    print(f"Spell cast: {elite.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {elite.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
