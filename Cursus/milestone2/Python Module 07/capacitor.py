from typing import cast
import ex1


def test_heal_creature(creature: ex1.HealingCreatureFactory):
    print("Testing Creature with healing capability")

    print("base:")
    heal_base_creature = creature.create_base("Sproutling")
    print(heal_base_creature.describe())
    print(heal_base_creature.attack())
    print(heal_base_creature.heal())

    print("evolved:")
    heal_evolved_creature = creature.create_evolved("Bloomelle")
    print(heal_evolved_creature.describe())
    print(heal_evolved_creature.attack())
    print(heal_evolved_creature.heal())


def test_transform_creature(creature: ex1.TransformCreatureFactory):
    print("\nTesting Creature with transform capability")

    print("base:")
    transform_base_creature = creature.create_base("Shiftling")
    print(transform_base_creature.describe())
    print(transform_base_creature.attack())
    print(transform_base_creature.transform())
    print(transform_base_creature.attack())
    print(transform_base_creature.revert())

    print("evolved:")
    transform_evolved_creature = creature.create_evolved("Morphagon")
    print(transform_evolved_creature.describe())
    print(transform_evolved_creature.attack())
    print(transform_evolved_creature.transform())
    print(transform_evolved_creature.attack())
    print(transform_evolved_creature.revert())


if __name__ == "__main__":
    heal_factory = ex1.HealingCreatureFactory()
    test_heal_creature(heal_factory)

    transform_factory = ex1.TransformCreatureFactory()
    test_transform_creature(transform_factory)
