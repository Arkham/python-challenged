#! /usr/bin/env python

# odd even

from PIL import Image

im = Image.open('11.jpg')
width, height = im.size

print width
print height

for x in range(width):
    for y in range(height):
        if (x+y) % 2 != 0:
            im.putpixel((x, y), 0)

im.save('test.jpg')
