#! /usr/bin/env python

import urllib
import re

seed = "12345"
base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

result = []
count = {}
for n in range(1, 400):
    count[seed] = count.get(seed, 0) + 1
    print "index: %d, count: %d, seed: %s" % (n, count[seed], seed)
    result.append(seed)

    page = urllib.urlopen(base_url + seed)
    seed = re.sub(r'[^0-9]*', '', page.read())

print result
