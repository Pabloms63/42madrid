from CreatureCard import CreatureCard


def main():
	print("\n=== DataDeck Card Foundation ===\n")

	print("\nTesting Abstract Base Class Design:\n")

	print("CreatureCard Info:")
	dragon = CreatureCard("Vermithor", 5, "Legendary", 250, 5000)
	print(dragon.get_card_info())

	print(f"\nPlaying {dragon.name} with 6 mana available:")
	print(f"Playable: {dragon.is_playable(6)}")
	print(f"Play result: {dragon.play()}")

	print(f"\n{dragon.name} attacks Human:")
	print(f'Attack result: {dragon.attack_target("Human")}')

	print("\nTesting insufficient mana (3 available):")
	human = CreatureCard("Pablo", 5, "Common", 25, 100)
	print(f"Playable: {human.is_playable(3)}")

	print("\nAbstract pattern successfully demonstrated!")

if __name__ == "__main__":
	main()