from S1E9 import Character


class Baratheon(Character):
	"""Baratheon family 🦌"""
	first_name = "Baratheon"
	is_alive = True

	def __init__(self, first_name, alive=True):
		"""Baratheon: init"""
		super().__init__(first_name, alive)
		self.family_name = "Baratheon"
		self.eyes = "blue"
		self.hairs = "black"

	def __str__(self):
		"""Baratheon: __str__"""
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

	def __repr__(self):
		"""Baratheon: __repr__"""
		return self.__str__()

	def die(self):
		"""Baratheon: set alive to False"""
		self.is_alive = False

class Lannister(Character):
	"""Lannister family 🦁"""
	first_name = "Lannister"
	is_alive = True

	"""Lannister: Docstring au top :D"""
	def __init__(self, first_name, alive=True):
		"""Lannister: init"""
		super().__init__(first_name, alive)
		self.family_name = "Lannister"
		self.eyes = "green"
		self.hairs = "blond"

	def __str__(self):
		"""Lannister: __str__"""
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

	def __repr__(self):
		"""Lannister: __repr__"""
		return self.__str__()

	def die(self):
		"""Lannister: set alive to False"""
		self.is_alive = False
	
	@classmethod
	def create_lannister(cls, first_name, alive=True):
		"""Lannister: create_lannister"""
		return cls(first_name, alive)
