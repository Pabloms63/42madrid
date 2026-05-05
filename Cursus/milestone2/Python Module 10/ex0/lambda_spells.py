from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(
        mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0}

    powers = list(map(lambda m: m['power'], mages))

    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2)
    }


if __name__ == "__main__":
    print("Testing artifact sorter...")
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Mystic Necklace', 'power': 65, 'type': 'relic'},
        {'name': 'Mortal Ring', 'power': 72, 'type': 'relic'}
    ]
    sorted_arts = artifact_sorter(artifacts)
    for a in sorted_arts:
        print(f"{a['name']} ({a['power']} power)")

    print(power_filter(sorted_arts, ))

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    print(" ".join(spell_transformer(spells)))
    stats = mage_stats(artifacts)
    print(
        f"\nMax_power: {stats['max_power']}"
        f"\nMin_power: {stats['min_power']}"
        f"\nAvg_power: {stats['avg_power']}"
    )
