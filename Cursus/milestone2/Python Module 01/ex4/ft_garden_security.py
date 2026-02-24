class SecurePlant:
	def __init__(self, name:str, height:int, age:int):
		self.__name = name
		self.__height = 0
		self.__age = 0
		print(f"Plant created: {self.__name}")
		#Inicializacion segura getter/setter
		self.set_height(height)
		self.set_age(age)

	#Getter height
	def get_height(self) -> int:
		return self.__height
	
	#Setter height
	def set_height(self, value:int):
		if value >= 0:
			self.__height = value
			print(f"Height updated: {self.__height}cm [OK]")
		else:
			print(f"\nInvalid operation attempted: height {value} [REJECTED]")
			print("Security: Negative height rejected")
		
	#Getter age
	def get_age(self) -> int:
		return self.__age

	#Setter age
	def set_age(self, value:int):
		if value >= 0:
			self.__age = value
			print(f"Age updated: {self.__age} days [OK]")
		else:
			print(f"\nInvalid operation attempted: age {value} [REJECTED]")
			print("Security: Negative height rejected")

	def get_info(self):
		print(f"\nCurrent plant: {self.__name} ({self.__height}cm {self.__age} days)")
	
if __name__ == "__main__":
	plant1 = SecurePlant("Rose", 25, 30)
	plant1.set_age(-8)
	plant1.get_info()