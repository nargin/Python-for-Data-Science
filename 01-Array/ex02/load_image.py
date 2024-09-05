from PIL import Image


def ft_load(path: str):
    """Load an image from a file into a 2D array of pixels."""
    img = Image.open(path)
    pixels = img.load()
    width, height = img.size
    print(f"Image size: {width} x {height} x {len(pixels[0, 0])}")
    return [[pixels[x, y] for x in range(width)] for y in range(height)]
