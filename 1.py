#! /usr/bin/env python

import string

def build_range(start_char, end_char):
    return ''.join([ chr(x) for x in xrange(ord(start_char), ord(end_char) + 1) ])

# source = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
source = "map"
orig = build_range('a', 'z')
dest = build_range('c', 'z') + "ab"

print source.translate(string.maketrans(orig, dest))
