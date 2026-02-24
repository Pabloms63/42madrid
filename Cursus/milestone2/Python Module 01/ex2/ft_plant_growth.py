class Plant:
	def __init__(self, name, height, days):
		self.name = name
		self.height = height
		self.days = days

	def get_info(self):
		print(f"{self.name}: {self.height}cm, {self.days} days old")
	def grow(self):
		self.height += 1
	def age(self):
		self.days += 1

#Forma 1
if __name__ == "__main__":
	count:int = 0
	plant1 = Plant("Rose", 25, 30)
	initial_height:int = plant1.height
	for day in range(1, 7):
		count += 1
		print(f"=== Day {day} ===")
		plant1.get_info()
		plant1.grow()
		plant1.age()
	growth:int = (plant1.height - initial_height)
	print(f"Growth this week: +{growth}cm\n")

#Forma 2
	count = 0
	plant2 = Plant("Sunflower", 80, 45)
	initial_height2:int = plant2.height
	print("=== Day 1 ===")
	plant2.get_info()
	for day in range(1, 8):
		plant2.grow()
		plant2.age()
	print("=== Day 7 ===")
	plant2.get_info()
	growth:int = (plant2.height - initial_height2)
	print(f"Growth this week: +{growth}cm")