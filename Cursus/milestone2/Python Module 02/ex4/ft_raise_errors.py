def check_plant(plant_name, water_level, sunlight_house):
    if plant_name is None:
        raise ValueError("Plant name cannot be empty")
    elif water_level < 0:
        raise ValueError(f"Water level {water_level} is too low (min 0)")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif sunlight_house < 2:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_house} is too low (min 2)")
    elif sunlight_house > 12:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_house} is too high (max 12)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plants_check():
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    try:
        check_plant("tomato", 6, 7)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting empty plant name...")
    try:
        check_plant(None, 6, 7)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        check_plant("tomato", 45, 7)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad sunlight hours...")
    try:
        check_plant("tomato", 6, 1)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


test_plants_check()
