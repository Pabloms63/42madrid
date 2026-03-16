if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    print(f"Player alice achievements: {alice}")

    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    print(f"Player bob achievements: {bob}")

    charlie = {
        'level_10', 'treasure_hunter',
        'boss_slayer', 'speed_demon', 'perfectionist'
        }
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    unique = alice.union(bob, charlie)
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}")

    common = alice.intersection(bob, charlie)
    print(f"\nCommon to all players: {common}")

    rare1 = alice - bob - charlie
    rare2 = bob - alice - charlie
    rare3 = charlie - alice - bob
    rare4 = rare1.union(rare2, rare3)
    print(f"Rare achievements (1 player): {rare4}")

    alice_bob_common = alice.intersection(bob)
    print(f"\nAlice vs Bob common: {alice_bob_common}")

    alice_unique = alice.difference(bob)
    print(f"Alice unique: {alice_unique}")

    bob_unique = bob.difference(alice)
    print(f"Bob unique: {bob_unique}")
