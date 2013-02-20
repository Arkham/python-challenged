#! /usr/bin/env python

import re

source = ''.join([ line.strip() for line in open('3.txt')])
print ''.join(re.findall('(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])', source))
