#!/opt/local/bin/python2.7

print "Welcome to the English to Pig Latin translator!"

original = raw_input("Please enter a word!")
size = len(original)

if size > 0 and original.isalpha():
	print original
	print size
else:
	print "Your word is either empty or has numbers in it, please use only alphabets."
