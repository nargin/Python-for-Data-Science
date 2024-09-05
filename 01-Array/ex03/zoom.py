from load_image import ft_load
from PIL import Image
import numpy


def resizer_errorless(array, points: list[int, int], size: list[int, int]):
    ret = numpy.zeros((size[0], size[1], 3), dtype=numpy.uint8)
    for y in range(size[0]):
        for x in range(size[1]):
            ret[y][x] = array[points[0] + y][points[1] + x]
    return ret


def zoom(array, coords: list[int, int], size: list[int, int]):
    """Zoom in or out of an image.
Args:
    img (str): Path to an image file.
    coords (tuple): Coordinates of the top-left corner of the zoomed area.
    size (tuple): Size of the zoomed area.
"""
    try:
        assert coords[0] >= 0 and coords[1] >= 0, "Coords must be positive."
        img = numpy.array(array)
        rows, cols, channels = img.shape
        assert coords[0] + size[0] <= rows, "Out of scope"
        assert coords[1] + size[1] <= cols, "Out of scope"
        resized = resizer_errorless(img, coords, size)
        print(f"resize shape: {resized.shape}")
        image = Image.fromarray(resized)
        image.save("zoomed.jpeg")

    except AssertionError as e:
        print(e)


def main():
    print(zoom.__doc__)
    zoom(ft_load("animal.jpeg"), (150, 450), (368, 400))


if __name__ == "__main__":
    main()
