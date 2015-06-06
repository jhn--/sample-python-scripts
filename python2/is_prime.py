# my original code here. its shit.
#def is_prime(x):
#	if (x < 2):
#		return False
#	else:
#		for i in range(1,x+1):
#			print str(x) + " / " + str(i)
#			if (x+1 / i == 1) and (x+1 / i == x+1):
#				print "True" + ", " + str(x)
#				return True
#			else:
#				print "False" + ", " + str(x)
#				return False

#correct answer
def is_prime(x):
	if (x < 2):
		return False
	for i in range(2,x):
		print i
		if (x%i) == 0:
			return False
	return True


print is_prime(5)
'''
Q & A

1 - What is "%"?

"%" is a mathematical operator called "modulus". "It returns the remainder of number x after it is divided by "number y". For example: "6%6" returns "0", "6%5" returns "1".

2 - Why is our range(2, x)?
As an example: If we were testing if "6" was a prime number, we would want to test if "6" divided by any of the numbers 2,3,4,5 yields a remainder of 0. If they do, we know "6" is not prime. In fact, when we test 6%3, we get a remainder of 0 and "return False". We don't want to test x%x because every number divided by itself yields a remainder of 0. We dont't want to test x%1 for the same reason.

3 - Why x < 2: 
We know every number less than 2, including negative numbers, are not prime, so we want to get that condition out of the way quick.

4 - Why doesn't "is_prime(2)" return False? 
Because with "2" assigned to "x" our range(2, x) == range(2, 2).
Which translates to "starting our range at '2', iterate forward, through the number right before '2', which is '1'. Because you can't go forward from '2' to '1', the program never iterates, the 'if' conditional statement never runs, and the program defaults to returning 'True'.
'''