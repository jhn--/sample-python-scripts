a = 0b1110
b = 0b101

a = [a for a in bin(a)]
b = [b for b in bin(b)]

if len(a) > len(b):
	b.insert(2,'0')
else:
	a.insert(2,'0')

print a
print b

z = []
for i,j in zip(a,b):
	if i==j:
		z.append(i)
	else:
		z.append('1')

print z
print "".join(z)