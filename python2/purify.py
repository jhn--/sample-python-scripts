def purify(x):
	z = []
	for i in x:
		if (i%2 == 0):
			z.append(i)
	return z

print purify([1,2,3])