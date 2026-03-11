def water_plants(plant_list):
    print("Opening watering system")

    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    plants1 = ["tree", "oak"]
    water_plants(plants1)
    print("Watering completed successfully!\n")

    print("\nTesting with error...")
    plants2 = [None, "oak"]
    water_plants(plants2)

    print("\nCleanup always happens, even with errors!")


test_watering_system()
