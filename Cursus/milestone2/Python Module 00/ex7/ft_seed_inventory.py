def ft_seed_inventory(seed_type: str, quantity: int, unit: str) ->None:
    if unit in ["packets", "grams", "area"]:
        print(seed_type.capitalize(), " seeds: ", quantity, " ", unit, " total")
    else:
        print("Unknown unit type")