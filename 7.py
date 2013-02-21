#! /usr/bin/env python

from PIL import Image

im = Image.open("7.png").crop((0,43,608,44))
colors = list(im.getdata())
colors = [ elem for index, elem in enumerate(colors) if index % 7 == 0]
print ''.join([ chr(elem[0]) for elem in colors ])

solution = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join([ chr(elem) for elem in solution ])
