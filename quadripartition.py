"""This module does blah blah."""
from math import sqrt
from PIL import Image

img = Image.open("resources/licorne1.bmp")
pixels = img.load()

def read_pixel(x, y):
    """
        Lit un pixels en valeur RGB

        :param x:
        :param y:
        :rtype tuple(r, g, b):
    """
    return pixels[x, y]

print read_pixel(2, 2)
