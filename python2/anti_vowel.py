def anti_vowel(x):
	z = []
	for i in x:
		if (i.lower() != 'a') and (i.lower() != 'e') and (i.lower() != 'i') and (i.lower() != 'o') and (i.lower() != 'u'):
			z.append(i)
	return ''.join(z)

print anti_vowel("Hey look Words!")