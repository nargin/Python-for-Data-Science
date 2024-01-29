from load_image import ft_load
from PIL import Image
import numpy
import PIL.ImageOps 

def ft_invert(array):
	"""Invert color of a picture"""
	rows, cols, channels = array.shape
	inverted = numpy.copy(array)
	max = 255
	for y in range(rows):
		for x in range(cols):
			for z in range(channels):
				inverted[y][x][z] = max - array[y][x][z]
	return inverted

def ft_blue(array):
	"""Blueing the picture"""
	blue = numpy.copy(array)
	blue[:, :, 0:2] = 0
	return blue

def ft_green(array):
	"""Blueing the picture"""
	green = numpy.copy(array)
	green[:, :, 0] = 0
	green[:, :, 2] = 0
	return green

def ft_red(array):
	"""Blueing the picture"""
	red = numpy.copy(array)
	red[:, :, 1] = 0
	red[:, :, 2] = 0
	return red

def ft_grey(array):
	"""Image become grey"""
	grey = numpy.copy(array)
	rows, cols, channels = grey.shape
	for y in range(rows):
		for x in range(cols):
			for z in range(channels):
				grey[y][x][z] = 1 if grey[y][x][z] > 128 else grey[y][x][z]
	return grey

def do_img(array, function, save_to):
	new = function(array)
	new = Image.fromarray(new)
	new.save(save_to + ".jpeg")

def main():
	img = ft_load("landscape.jpg")
	do_img(img, ft_invert, "inverted")
	do_img(img, ft_blue, "blueing")
	do_img(img, ft_green, "greening")
	do_img(img, ft_red, "reding")
	do_img(img, ft_grey, "grey")

if __name__ == "__main__":
	main()
