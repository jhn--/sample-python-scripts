#! /usr/bin/env python

numlist = [1,3,5,7,9]

def sumList(numlist):
	if len(numlist) == 1:
		#option 1
		print "hey: %d" % (numlist[0])
		return numlist[0]
	else:
		#option 2
		#ace = numlist[0] + sumList(numlist[1:])
		#print "ace: %d" % (ace)
		#print "ace: %d = %d + %s" % (ace, numlist[0], str(numlist[1:]))
		print "%d + %s" % (numlist[0], str(numlist[1:]))
		return numlist[0] + sumList(numlist[1:])

print sumList(numlist)

'''
sumList([1,3,5,7,9])
if len of numlist == 1, then return its one and only element

else

take its first element, add it to the result of sumList() with numlist without its first element.

sumList() will have numlist with the first element gone.

sumList() will check if there's only 1 element in numlist, if there is only one, return it(where???????), 
if not, take out its first element of this already shortened list, and 
submit it to itself again.

1 + [3, 5, 7, 9] opt2
3 + [5, 7, 9] opt2
5 + [7, 9] opt2
7 + [9] opt2
hey: 9 opt1
25

'''