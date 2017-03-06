"""This module does blah blah."""
from math import sqrt
from PIL import Image

img = Image.open("resources/licorne1.bmp")
px = img.load()

def read_pixel(pixels, x, y):
    """
        Lit un pixels en valeur RGB

        :param x:
        :param y:
        :rtype tuple(r, g, b):
    """
    return pixels[x, y]

print read_pixel(px, 2, 2)
