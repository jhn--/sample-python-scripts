#! /usr/bin/python

import string

#a = "ipsum loren, blahblahblah"
a = raw_input("enter a lower string sentence: ")
b = []
#print list(enumerate(a))											#show index and value, for debugging purposes.
for i, j in list(enumerate(a)):										#add index to the list, a.
#	print str(i)+", "+j 											#show index and value, for debugging purposes.
	if (i % 2) == 0:												#if index is divisible to 0 by 2, change it to != to alternate the letters to be upper()
		b.append(string.upper(j))									#add the upper case to the new list, b.
	else:
		b.append(j)													#continue adding letter to new list, b, even if index representing it is not divisible by 2
c = ''.join(b)
print c

d = string.swapcase(c)
print d