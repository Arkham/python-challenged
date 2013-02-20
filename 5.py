#! /usr/bin/env python

import pickle

content = pickle.load(open('5.p'))
for line in content:
    print ''.join([ elem[0] * elem[1] for elem in line ])
