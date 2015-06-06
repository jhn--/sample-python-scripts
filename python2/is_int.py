#!/usr/bin/python

def is_int(x):
	print x
	y = x % 2
	print "y = " + str(y)
	if (y == 1) or (y == 0) or (y == 1.0) or (y == 0.0):
		print True
	else:
		print False
#	for i in str(y):
#		while (i != "1") and (i != ".") and (i != "0"):
#			print False
#			break
#	else:
#		print True


is_int(987.00100)