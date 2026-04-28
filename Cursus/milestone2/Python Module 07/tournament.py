from ex0.base import CreatureFactory
from ex0.flame import FlameFactory
from ex0.aqua import AquaFactory
from ex1.heal import HealingCreatureFactory
from ex1.transform import TransformCreatureFactory
from ex2.base_strategy import BattleStrategy
from ex2.strategies import AggresiveStrategy, DefensiveStrategy, NormalStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy, str]]):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print("\n* Battle *")

    for x in range(len(opponents)):
        for y in range(x + 1, len(opponents)):
            factory_x, strategy_x, name_x = opponents[x]
            op1 = factory_x.create_base(name_x)

            factory_y, strategy_y, name_y = opponents[y]
            op2 = factory_y.create_base(name_y)

            try:
                print(
                    f"{op1.name} is a {op1.creture_type} "
                    f"type {op1.__class__.__mro__[1].__name__}"
                )
                print("vs.")
                print(
                    f"{op2.name} is a {op2.creture_type} type "
                    f"{op2.__class__.__mro__[1].__name__}"
                )
                print("now fight!")
                strategy_x.is_valid(op1)
                strategy_x.act(op1)
                strategy_y.is_valid(op2)
                strategy_y.act(op2)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    # First Tournament
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    flame_factory = FlameFactory()
    heal_factory = HealingCreatureFactory()

    normal_strategy = NormalStrategy()
    def_strategy = DefensiveStrategy()

    opponents0 = [
        (flame_factory, normal_strategy, "Flameling"),
        (heal_factory, def_strategy, "Sproutling")
    ]

    battle(opponents0)

    # Second Tournament
    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    heal_factory = HealingCreatureFactory()

    aggresive_strategy = AggresiveStrategy()

    opponents1 = [
        (flame_factory, aggresive_strategy, "Flameling"),
        (heal_factory, def_strategy, "Sproutling")
    ]

    battle(opponents1)

    # Third Tournament
    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    aqua_factory = AquaFactory()
    transform_factory = TransformCreatureFactory()

    opponents2 = [
        (aqua_factory, normal_strategy, "Aquabub"),
        (heal_factory, def_strategy, "Sproutling"),
        (transform_factory, aggresive_strategy, "Shiftling")
    ]

    battle(opponents2)
