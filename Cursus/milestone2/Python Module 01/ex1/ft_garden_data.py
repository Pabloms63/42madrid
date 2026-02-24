class Plant:
	def __init__(self, name, height, days):
		self.name = name
		self.height = height
		self.days = days
		print(f"{name}: {height}cm, {days} days old")

if __name__ == "__main__":
	print("=== Garden Plant Registry ===")
	plant1 = Plant("Rose", 25, 30)
	plant2 = Plant("Sunflower", 80, 45)
	plant3 = Plant("Cactus", 15, 120)