from abc import ABC, abstractmethod

class Character(ABC):
	"""Character class name: str, is_alive: bool"""
	name = ""
	is_alive = True

	@abstractmethod
	def die(self):
		"""Mort"""
		pass
	def __init__(self, name, alive=True):
		"""init la"""
		self.name = name
		self.is_alive = alive		

class Stark(Character):
	"""Docstring au top :D"""
	def die(self):
		"""Mort 2"""
		self.alive = False