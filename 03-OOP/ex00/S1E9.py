from abc import ABC, abstractmethod

class Character(ABC):
	"""Character class name: str, is_alive: bool"""
	@abstractmethod
	def die(self):
		
		

class Stark(Character):