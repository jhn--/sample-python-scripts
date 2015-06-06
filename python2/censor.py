def censor(text, word):
	lala = len(word)
	text = text.split()
	word = word.split()
	z = []
	for i in text:
		if i in word:
			i = "*"*lala
		z.append(i)
	return ' '.join(z)

print censor("this hack is wack hack", "hack")

'''
def censor(text, word):
	text = text.split()
	print text

print censor("this hack is wack hack", "hack")
'''
