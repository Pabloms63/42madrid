class GardenManager:
    def __init__(self, gardens):
        self.gardens = gardens

    @classmethod
    def create_garden_network(cls, gardens):
        return cls(gardens)

    def show_garden_scores(self):
        scores = []
        for garden in self.gardens:
            score = self.GardenStats.calculate_score(garden)
            scores.append(f"{garden.owner_name}: {score}")
        print("Garden scores - " + ", ".join(scores))

    def show_height_validation_test(self):
        valid = True
        for garden in self.gardens:
            if not GardenManager.GardenStats.validation_height(garden):
                valid = False
                break
        print(f"Height validation test: {valid}")

    def total_gardens(self):
        print(f"Total gardens managed: {len(self.gardens)}")

    class GardenStats:
        @staticmethod
        def validation_height(garden):
            for p in garden.plants:
                if p.height < 0:
                    return False
            return True

        @staticmethod
        def calculate_score(garden):
            score = 0
            for p in garden.plants:
                score += p.height
                if isinstance(p, PrizeFlower):
                    score += p.prize_points
                if isinstance(p, FloweringPlant):
                    if p.blooming:
                        score += 5
            return score


class Garden():
    def __init__(self, owner_name, plants):
        self.owner_name = owner_name
        self.plants = plants

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def help_plants_grow(self):
        print(f"\n{self.owner_name} is helping all plants grow...")
        total_growth = 0
        for p in self.plants:
            old_height = p.height
            p.grow()
            total_growth += p.height - old_height
        return (total_growth)

    def generate_report(self, total_growth):
        print(f"\n=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        regular = 0
        flowering = 0
        prize_flower = 0
        for p in self.plants:
            if isinstance(p, PrizeFlower):
                prize_flower += 1
            elif isinstance(p, FloweringPlant):
                flowering += 1
            elif isinstance(p, Plant):
                regular += 1
            p.get_info()

        print(
            f"\nPlants added: {len(self.plants)}, "
            f"Total growth: {total_growth}cm")
        print(
            f"Plant types: {regular} regular, {flowering} "
            f"flowering, {prize_flower} prize flowers\n"
        )


class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self):
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color, blooming):
        super().__init__(name, height, age)
        self.color = color
        self.blooming = blooming

    def get_info(self):
        if self.blooming is True:
            print(
                f"- {self.name}: {self.height}cm, "
                f"{self.color} flowers (blooming)"
                )
        else:
            print(
                f"- {self.name}: {self.height}cm, "
                f"{self.color} flowers (not blooming)"
                )


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, blooming, prize_points):
        super().__init__(name, height, age, color, blooming)
        self.prize_points = prize_points

    def get_info(self):
        if self.blooming is True:
            print(
                f"- {self.name}: {self.height}cm {self.color} "
                f"flowers (blooming), Prize points: {self.prize_points}"
                )
        else:
            print(
                f"- {self.name}: {self.height}cm {self.color} "
                f"flowers (not blooming), Prize points: {self.prize_points}"
                )


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    # Jardin 1
    garden1 = Garden("Pablo", [])
    plant1 = Plant("Oak Tree", 210, 10235)
    flower1 = FloweringPlant("Rose", 26, 240, "red", True)
    prize_flower1 = PrizeFlower("Sunflower", 51, 325, "yellow", False, 10)
    garden1.add_plant(plant1)
    garden1.add_plant(flower1)
    garden1.add_plant(prize_flower1)
    total_growth = garden1.help_plants_grow()
    garden1.generate_report(total_growth)

    # Jardin 2
    garden2 = Garden("Amancio", [])
    plant2 = Plant("Holm Oak", 101, 12500)
    garden2.add_plant(plant2)
    total_growth = garden2.help_plants_grow()
    garden2.generate_report(total_growth)

    # GardenManager
    boss = GardenManager.create_garden_network([garden1, garden2])
    boss.show_height_validation_test()
    boss.show_garden_scores()
    boss.total_gardens()
