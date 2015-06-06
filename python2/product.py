def product(x):
	prod = 1
	for i in x:
		print str(prod) + "*=" + str(i)
		prod *= i
	return prod

print product([4, 5, 5])