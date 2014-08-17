#! /usr/bin/python

import string

#a = "ipsum loren, blahblahblah"
a = raw_input("enter a lower string sentence: ")
b = list(a)

print list(b)

for i in range(0, len(b), 2):
	b[i] = string.upper(b[i])

print "a: " + a

print "b: " + str(b)

c = ''.join(b)
print "c: " + c

d = string.swapcase(c)
print "d: " + d	