def factorial(x):
	if range(x) == 1:
		return 0
	else:
		for i in range(1,x):
			print str(x) + " * " + str(i)
			x *= i
		return x

print factorial(10)



#the approach other people have thought up is ingenious, 
#what they did was remove the 0 from the list, x by using the command range(1, x)
#then they multiply the last value, x, with the increasing i.