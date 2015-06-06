def remove_duplicates(x):
	print x
	z = []
	for i in x:
		print "x" + str(i)
		if i not in z:
			z.append(i)
	return z

'''
go through every element in list
take each element and compare w the new list 
if element not in new list
append into new list
else if element in new list, move on.
the [not in] syntax is very impt =,=
'''

print remove_duplicates([1,1,2,2])