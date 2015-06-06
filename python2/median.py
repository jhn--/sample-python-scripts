def median(x):
	x = sorted(x)
	print x
	if ((len(x)%2) == 1):
		y = len(x)/2
		return x[y]
	else:
		e =  x[(len(x)/2)]
		f =  x[((len(x)-1)/2)]
#		y = (x[(len(x)/2)] + x[((len(x)-1)/2)]/2.0)
		y = (e+f)/2.0
		return y


print median([7,12,3,1,6,2,5])
print median([4, 5, 5, 4])
print median([1, 34, 1, 6, 8, 0])