from math import pi
from PIL import Image
im = Image.open("gray-img.jpeg")
pixels = im.load()
print(pixels[20,20])
