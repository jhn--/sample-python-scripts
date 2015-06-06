def count(a, b):
	total = 0
	for i in a:
		if i == b:
			total +=1
	return total

print count([1,2,1,1],1)