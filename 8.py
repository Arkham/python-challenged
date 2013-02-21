#! /usr/bin/env python

import bz2

magic_dict = {
    "\x1f\x8b\x08": "gz",
    "\x42\x5a\x68": "bz2",
    "\x50\x4b\x03\x04": "zip"
    }

max_len = max(len(x) for x in magic_dict)

def string_type(string):
    for magic, filetype in magic_dict.items():
        if string.startswith(magic):
            return filetype
    return "no match"

user = "BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
pw = "BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"

print "user type: ", string_type(user)
print "string type: ", string_type(pw)

# original_data = 'This is it.'
# print 'Original     :', len(original_data), original_data

# compressed = bz2.compress(original_data)
# print 'Compressed   :', len(compressed), compressed

# decompressed = bz2.decompress(compressed)
# print 'Decompressed :', len(decompressed), decompressed

print "user: ", bz2.decompress(user)
print "pw: ", bz2.decompress(pw)
