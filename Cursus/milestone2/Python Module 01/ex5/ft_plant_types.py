class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age

class Flower(Plant):
	def __init__(self, name, height, age, color):
		super().__init__(name, height, age)
		self.color = color
	
	def bloom(self):
		if self.color == "red":
			print(f"{self.name} is blooming beautifully!\n")
		else:
			print(f"{self.name} has not yet bloomed\n")
	
	def get_info(self):
		print(f"{self.name}(Flower): {self.height}cm, {self.age} days, {self.color} color")
		
class Tree(Plant):
	def __init__(self, name, height, age, trunk_diameter):
		super().__init__(name, height, age)
		self.trunk_diameter = trunk_diameter

	def produce_shade(self):
		shade = ((self.height + self.trunk_diameter) / 7)
		print(f"{self.name} provides {shade:.0f} square meters of shade\n")

	def get_info(self):
		print(f"{self.name}(Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")

class Vegetable(Plant):
	def __init__(self, name, height, age, harvest_season, nutritional_value):
		super().__init__(name, height, age)
		self.harvest_season = harvest_season
		self.nutritional_value = nutritional_value

	def get_info(self):
		print(f"{self.name}(Vegetable): {self.height}cm, {self.age} days, {self.harvest_season}\n{self.name} is rich in {self.nutritional_value}\n")

if __name__ == "__main__":
	#Flowers
	flower1 = Flower("Rose", 25, 30, "red")
	flower1.get_info()
	flower1.bloom()
	flower2= Flower("Orchid", 20, 28, "white")
	flower2.get_info()
	flower2.bloom()

	#Trees
	tree1 = Tree("Oak", 500, 1825, 50)
	tree1.get_info()
	tree1.produce_shade()
	tree2 = Tree("Pine", 720, 3500, 72)
	tree2.get_info()
	tree2.produce_shade()

	#Vegetables
	vegetable1 = Vegetable("Tomato", 80, 90, "summer harvest", "vitamin c")
	vegetable1.get_info()
	vegetable2 = Vegetable("Carrot", 120, 102, "spring harvest", "vitamin a")
	vegetable2.get_info()
	