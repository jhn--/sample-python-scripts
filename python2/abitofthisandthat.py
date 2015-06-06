a = 0b1110
b = 0b101

a = bin(a)
b = bin(b)

aa = a[2:len(a)]
bb =  b[2:len(b)]

#print aa
#print bb

if (len(aa) - len(bb)) > 0:
	for i in range((len(aa) - len(bb))):
		bb = "0" + "" + bb
else:
	for i in range((len(bb) - len(aa))):
		aa = "0"+ "" + aa

aa = [t for t in str(aa)]
bb = [u for u in str(bb)]

z = []
for x, y in zip(aa,bb):
	if x == y:
		z.append(x)
	else:
		z.append('0')

z = "0b" + "".join(z)
print z

z = int(z,2)
z = bin(z)
print z