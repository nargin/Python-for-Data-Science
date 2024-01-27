from load_image import ft_load
from PIL import Image
import numpy


def zoom(img, coords: list[int, int], size: list[int, int]):
	"""Zoom in or out of an image.
Args:
	img (str): Path to an image file.
	coords (tuple): Coordinates of the top-left corner of the zoomed area.
	size (tuple): Size of the zoomed area.
"""
	try:
		assert coords[0] >= 0 and coords[1] >= 0, "Coords must be positive."
		img = numpy.array(ft_load(img))
		rows, cols, channels = img.shape
		assert coords[0] + size[0] <= rows, "Out of scope"
		assert coords[1] + size[1] <= cols, "Out of scope"
		

	except AssertionError as e:
		print(e)

def main():
	print(zoom.__doc__)
	zoom("animal.jpeg", (400, 400), (368, 100))


if __name__ == "__main__":
	main()