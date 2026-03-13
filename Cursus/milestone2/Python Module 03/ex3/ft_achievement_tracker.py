print("=== Achievement Tracker System ===")

alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
print(f"Player alice achievements: {alice}")

bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
print(f"Player bob achievements: {bob}")

charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}
print(f"Player charlie achievements: {charlie}")

print("\n=== Achievement Analytics ===")
set1 = alice.union(bob)
set2 = set1.union(charlie)
print(f"All unique achievements: {set2}")
print(f"Total unique achievements: {len(set2)}")

print(f"Common to all players: {}")