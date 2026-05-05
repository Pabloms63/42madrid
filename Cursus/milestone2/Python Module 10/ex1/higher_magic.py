from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spell(target: str, power: int) -> list[str]:
        return [s(target, power) for s in spells]
    return sequence_spell


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    print("Testing spell combiner...")
    combo = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combo('Dragon', 50)}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original (power 10): {fireball('Goblin', 10)}")
    print(f"Amplified (power 10 -> 30): {mega_fireball('Goblin', 10)}")

    print("\nTesting conditional caster...")
    strong_only = conditional_caster(lambda t, p: p > 20, fireball)
    print(f"Power 30: {strong_only('Orc', 30)}")
    print(f"Power 10: {strong_only('Orc', 10)}")

    print("\nTesting spell sequence...")
    party_spells = spell_sequence([fireball, heal, fireball])
    results = party_spells("Hydra", 100)
    for res in results:
        print(f"Sequence: {res}")
