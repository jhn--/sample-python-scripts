#!/opt/local/bin/python2.7
args = raw_input("enter a number!")
args = int(args)

def by_three(args):
	if args % 3 == 0:
		return cube(args)
	else:
		print str(args) + " is not divisible by 3"
		return False

def cube(args):
	args = args ** 3
	print args
	return args

#by_three(11)
#by_three(12)
#by_three(13)
by_three(args)