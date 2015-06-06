#yet another piece of rubbish code by yours truly.
'''
def reverse(x):
	print x
	j = []
	for i in x:
		j.append(i)
	print j
	print "h"
	print range(len(j))
	k = []
	for i in j:
		while (i==j):
			k.append(i)
	print k
reverse("hello")
'''

#some smart guy's code
def reverse(x):
	l = []
	for i in x:
		l.insert(0,i)
	return ''.join(l) 
	print ''.join(l)

reverse("Python!")