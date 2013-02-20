#! /usr/bin/env python

import collections

source = ''.join([ line.strip() for line in open('2.txt') ])

result = collections.OrderedDict()
for char in source:
    result[char] = result.get(char, 0) + 1

average = len(source) // len(result)

print ''.join([ char for char, count in result.iteritems() if count < average ])
