from load_image import ft_load
from PIL import Image
import numpy
import PIL.ImageOps 

def ft_invert(array):
	"""Invert color of a picture"""
	array = numpy.array(array)
	rows, cols, channels = array.shape

	for y in rows:
		for x in cols:
			

def main():
	img = ft_load("landscape.jpeg")
	new = ft_invert(img)

if __name__ == "__main__":
	main()
