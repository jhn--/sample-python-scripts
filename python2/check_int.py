#!/opt/local/bin/python2.7

"""x=raw_input("enter number")

def distance_from_zero(x):
	if type(x) == "int" or "float":
		return abs(x)
		print abs(x)
	else:
		return "This isn't an interger or a float!"

distance_from_zero(99999.99)
"""

def distance_from_zero(x):
#apparently, there is no differences between inserting double quotes ("int") or no double quotes (int) at the line below
	if type(x) == int or float:
		return abs(x)
	else:
		return "This isn't an interger or a float!"

print distance_from_zero(-.09)