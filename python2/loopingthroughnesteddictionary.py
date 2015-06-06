#! /usr/bin/env python

dict2 = {'new jersey': {'mercer county': {'plumbers': 3, 'programmers': 81}, 'middlesex county': {'programmers': 81, 'salesmen': 62}}, 'new york': {'queens county': {'plumbers': 9, 'salesmen': 36}}}
'''
for i in dict2:
	print i 																	#new jersey, new york
	if len(dict2[i]) != 0:
		for z in dict2[i]:
			print "\t", z														#mercer, middlesex, queens county
			if len(dict2[i][z]) != 0:
				for y in dict2[i][z]:
					print "\t\t", y, dict2[i][z][y] 							#
			else:
				pass
	else:
		pass
'''

for i in dict2:
	print i
	for z in dict2[i]:
		print "|-", z
		for y in dict2[i][z]:
			print "    |-", y, dict2[i][z][y]