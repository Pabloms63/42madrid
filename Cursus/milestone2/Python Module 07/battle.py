import ex0
from ex0 import base


def test_factory_flame(factory: base.CreatureFactory, name1: str, name2: str):
    print("Testing factory")
    creature_base = factory.create_base(name1)
    creature_evolved = factory.create_evolved(name2)

    print(creature_base.describe())
    print(creature_base.attack())

    print(creature_evolved.describe())
    print(creature_evolved.attack())


def test_factory_aqua(factory: base.CreatureFactory, name1: str, name2: str):
    print("\nTesting factory")
    creature_base = factory.create_base(name1)
    creature_evolved = factory.create_evolved(name2)

    print(creature_base.describe())
    print(creature_base.attack())

    print(creature_evolved.describe())
    print(creature_evolved.attack())


def testing_battle(
    factory1: base.CreatureFactory, factory2: base.CreatureFactory
):
    print("\nTesting battle")
    creature1 = factory1.create_base("Flameling")
    creature2 = factory2.create_base("Aquabub")

    print(creature1.describe())
    print("vs.")
    print(creature2.describe())
    print("fight!")
    print(creature1.attack())
    print(creature2.attack())


if __name__ == "__main__":
    creature_flame = ex0.FlameFactory()
    test_factory_flame(creature_flame, "Flameling", "Pyrodon")

    creature_aqua = ex0.AquaFactory()
    test_factory_aqua(creature_aqua, "Aquabub", "Torragon")

    testing_battle(creature_flame, creature_aqua)
