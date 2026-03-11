class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant_name):
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")

        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self):
        print("Opening watering system")

        try:
            if not self.plants:
                raise WaterError("No plants to water :C")

            for p in self.plants:
                print(f"Watering {p} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant, water, sun):
        if water < 0:
            raise ValueError(f"Water level {water} is too low (min 0)")
        elif water > 10:
            raise ValueError(f"Water level {water} is too high (max 10)")
        elif sun < 2:
            raise ValueError(
                f"Error: Sunlight hours {sun} is too low (min 2)")
        elif sun > 12:
            raise ValueError(
                f"Error: Sunlight hours {sun} is too high (max 12)")

        print(f"{plant}: healthy (water: {water}, sun: {sun})")


def test_garden_management():
    print("=== Garden Management System ===")

    garden = GardenManager()
    print("\nAdding plants to garden...")
    try:
        garden.add_plant("tomato")
        garden.add_plant("lettuce")
        garden.add_plant("")
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    try:
        garden.water_plants()
    except WaterError as e:
        print(f"Error wateringing plant: {e}")

    print("\nChecking plant health...")
    try:
        garden.check_plant_health("tomato", 5, 8)
        garden.check_plant_health("lettuce", 5, 15)
    except ValueError as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")

    print("\nGarden management system test complete")


test_garden_management()
