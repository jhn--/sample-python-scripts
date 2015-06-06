def digit_sum(n):
	n = str(n)
	nlist = []
	for i in n:
		nlist.append(i)
	print nlist
	newn = 0
	for a in nlist:
		newn += int(a)
	print str(newn)

digit_sum(434)