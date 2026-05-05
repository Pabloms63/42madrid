from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total_power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    _vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        _vault[key] = value

    def recall(key: str) -> Any:
        return _vault.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Add 30 more: {acc(30)}")

    print("\nTesting enchantment factory...")
    flame_enchant = enchantment_factory("Flaming")
    ice_enchant = enchantment_factory("Frozen")
    print(flame_enchant("Sword"))
    print(ice_enchant("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
