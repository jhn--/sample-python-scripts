#!/opt/local/bin/python2.7

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
	print original
	word = original.lower()
	first = word[0]
	if first == "a" or first == first == "e" or first == "i" or first == "o" or first == "u" or first == "A" or first == "E" or first == "I" or first == "O" or first == "U":
		print "vowel"
		new_word = word + pyg
		print new_word
	else:
		print "cosonant"
		last = len(word) - 1
		print last
		new_word = word[1:] + first + pyg
		print "new_word = " + new_word
else:
	print 'empty'