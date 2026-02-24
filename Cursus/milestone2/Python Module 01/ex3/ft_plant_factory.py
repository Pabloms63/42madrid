class Plant:
	def __init__(self, name, height, days):
		self.name = name
		self.height = height
		self.days = days
		print(f"Created: {name}: ({height}cm, {days} days)")

if __name__ == "__main__":
	print("=== Plant Factory Output ===")
	plants_data = [
		("Rose", 25, 30),
		("Oak", 200, 365),
		("Cactus", 5, 90),
		("Sunflower", 80, 45),
		("Fern", 15, 120)
	]

	plants = [Plant(name, h, d) for name, h, d in plants_data]
	print(f"\nTotal plants created: {len(plants_data)}")
	