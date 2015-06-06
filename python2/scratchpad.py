#! /usr/bin/env python

#----------------------------#dictionary#----------------------------#

dict1 = {1: "happy", 2: "world", 3: "winning", 4:"yay"}

for i in dict1.keys():
	print dict1[i]
happy
world
winning
yay

dict1.keys()
[1,2,3,4]

dict1.values()
['happy', 'world', 'winning', 'yay']

dict2 = {'new jersey': {'mercer county': {'plumbers': 3, 'programmers': 81}, 'middlesex county': {'programmers': 81, 'salesmen': 62}}, 'new york': {'queens county': {'plumbers': 9, 'salesmen': 36}}}
'''
dict2 = {'new jersey': 
			{'mercer county': 
				{'plumbers': 3, 
				'programmers': 81}, 
			'middlesex county': 
				{'programmers': 81, 
				'salesmen': 62}}, 
		'new york': 
			{'queens county': 
				{'plumbers': 9, 
				'salesmen': 36}}}
'''
for key in dict2.keys():
	print key

for i in dict2:
    print i
    if len(dict2[i]) != 0:
        for z in dict2[i]:
            print "\t", z
            if len(dict2[i][z]) != 0
                for y in dict2[i][z]:
                    print "\t\t", y, "\n\t\t\t", dict2[i][z][y]
            else:
                pass
    else:
        pass


#----------------------------#os.path#----------------------------#

import os

mypath = os.getcwd()
mypath1 = os.path.dirname(mypath)
newfolder = raw_input("enter a folder: ")

newpath = os.path.join(mypath1, newfolder)
if os.path.exists(newpath) == False:
	os.mkdir(newpath)

#----------------------------#nested list#----------------------------#

nestlist = ['a', 'b', [1,2,3]]