from abc import ABC, abstractmethod

class Character(ABC):
	"""Character class name: str, is_alive: bool"""
	name = ""
	alive = True

	@abstractmethod
	def die(self):
		pass
	def __init__(self, name, alive=True):
		self.name = name
		self.alive = alive		

class Stark(Character):
	def die(self):
		self.alive = False