import numpy
from PIL import Image
from load_image import ft_load

def rotate(img):
	img = numpy.array(ft_load(img))
	return numpy.rot90(img)

def	main():
	img = rotate("animal.jpeg")
	img = Image.fromarray(img)
	img.save("rotated.jpeg")

if __name__ == "__main__":
	main()