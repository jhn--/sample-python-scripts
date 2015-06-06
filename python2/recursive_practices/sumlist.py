#! /usr/bin/env python

numlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

def sumList(numlist):
	sum = 0
	for i in numlist:
		print "%d + %d" % (sum, i)
		sum += i
	return sum

print sumList(numlist)