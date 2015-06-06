#!/usr/bin/python

thing = "spam!"

for c in thing:
    print c
    
word = "eggs!"

for i in word:
	print i

#what will happen here is, because i continues to be inside the variable word, it will continue printing.
#however, as we know, i will increment, in a while & for loop, in while it will remain at the last location of the variable and because it fulfills the requirement of being IN the variable it will continue to print itself.
#while i in word:
#	print i