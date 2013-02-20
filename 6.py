#! /usr/bin/env python

import re
from zipfile import ZipFile

comments = {}
with ZipFile('6/6.zip', 'r') as myzip:
    for info in myzip.infolist():
        comments[info.filename] = info.comment

folder = "6/"
current = '90052'
result = []

while (current != ''):
    current += ".txt"
    result.append(comments[current])

    file = open(folder + current)
    source = file.read()

    current = re.sub(r'[^0-9]*', '', source)

print ''.join(result)
