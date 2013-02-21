#! /usr/bin/env python

from itertools import *

def find_next(start):
    result = []

    for key, group in groupby(start):
        group_len = len(list(group))
        result.append("%d%s" % (group_len, key))

    return ''.join(result)

start = '1'
for n in range(30):
    start = find_next(start)
    print len(start), start
