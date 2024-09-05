from PIL import Image
import numpy


def ft_load(path: str):
    """Load an image from a file into a 2D array of pixels."""
    try:
        img = Image.open(path)
        pixel_content = numpy.array(img)
        rows, cols, channels = pixel_content.shape

        print("Image loaded from path: " + path)
        print(f"Image size: {rows} x {cols} x {channels}")
        return pixel_content

    except Exception as e:
        print(e)
