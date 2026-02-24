class GardenManager:
	def __init__(self, gardens):
		self.gardens = gardens

	class GardenStats:
		pass
	
class Garden():
	def __init__(self, owner_name, plants):
		self.owner_name = owner_name
		self.plants = plants

	def add_plant(self, plant):
		self.plants.append(plant)
		print(f"Added {plant.name} to {self.owner_name}'s garden")

	def help_plants_grow(self):
		print(f"{self.owner_name} is helping all plants grow...")
		total_growth = 0
		for p in self.plants:
			old_height = p.height
			p.grow()
			total_growth += p.height - old_height
		return (total_growth)

	def generate_report(self, total_growth):
		print(f"=== {self.owner_name}'s Garden Report ===")
		print("Plants in garden:")
		regular = 0
		flowering = 0
		prize_flower = 0
		for p in self.plants:
			if type(p) == Plant:
				regular += 1
			elif type(p) == FloweringPlant:
				flowering += 1
			elif (type(p) == PrizeFlower):
				prize_flower += 1
			p.get_info()

		print(f"\nPlants added: {len(self.plants)}, growth: {total_growth}cm")
		print(f"Plant types: {regular} regular, {flowering} flowering, {prize_flower} prize flowers\n")

class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age
	
	def grow(self):
		self.height += 1
		print(f"{self.name} grew 1 cm")

	def get_info(self):
		print(f"- {self.name}: {self.height}cm")

class FloweringPlant(Plant):
	def __init__(self, name, height, age, color, blooming):
		super().__init__(name, height, age)
		self.color = color
		self.blooming = blooming

	def get_info(self):
		if self.blooming == True:
			print(f"- {self.name}: {self.height}, {self.color}flowers ({self.blooming})")
		else:
			print(f"- {self.name}: {self.height}, {self.color}flowers ({self.blooming})")

class PrizeFlower(FloweringPlant):
	def __init__(self, name, height, age, color, blooming, prize_points):
		super().__init__(name, height, age, color, blooming)
		self.prize_points = prize_points

	def get_info(self):
		print(f"- {self.name}: {self.height}cm {self.color} flowers ({self.blooming}), Prize points: {self.prize_points}")

if __name__ == "__main__":
	#Plantas
	plant1 = Plant("Oak Tree", 101, 12500)
	flower1 = FloweringPlant("Rose", 26, 240, "red", "blooming")
	prize_flower1 = PrizeFlower("Sunflower", 51, 325, "yellow", "not blooming", 10)

    #Creo lista vacía
	plants = []

	#Jardines
	garden1 = Garden("Pablo", plants)
	garden1.add_plant(plant1)
	print("\n")
	total_growth = garden1.help_plants_grow()
	garden1.generate_report(total_growth)

	#GardenManager
	boss = GardenManager(garden1)
