from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
	"""King: 🤴"""

	def __init__(self, first_name, alive=True):
		super().__init__(first_name, alive)
		self.eyes = "red"
		self.hairs = "green"

	def set_eyes(self, eyes):
		self.eyes = eyes
	
	def set_hairs(self, hairs):
		self.hairs = hairs
	
	def get_eyes(self):
		return self.eyes
	
	def get_hairs(self):
		return self.hairs
