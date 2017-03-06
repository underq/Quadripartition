from quadripartition import read_pixel
from PIL import Image

img = Image.open("resources/licorne1.bmp")
px = img.load()

def test_answer():
    assert read_pixel(px, 1, 1) == px[1, 1]
