def remove_duplicates(x):
	print x
	z = []
	print len(z)
	for i in x:
		print "x" + str(i)
		for a in z:
			print "z" + str(a)
			if (i == a):
				break
			elif (z[a] == z[len(z)]):
				z.append(i)
	print z

'''
go through every element in list
take each element and compare w the new list 
if element not in new list
append into new list
else if element in new list, move on.
'''

remove_duplicates([1,1,2,2])