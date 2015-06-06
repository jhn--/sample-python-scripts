'''

A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another 100 steps, turns another random amount, etc. A social science student records the angle of each turn before the next 100 steps are taken. Her experimental data is [160, -43, 270, -97, -43, 200, -940, 17, -86]. (Positive angles are counter-clockwise.) Use a turtle to draw the path taken by our drunk friend.

'''

#! /usr/bin/env python

import turtle

wn = turtle.Screen()
pirate = turtle.Turtle()
pirate.speed(1)

angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

def drunkenpath(obj):
	heading = 0
	for i in angles:
		'''							#probably not necessary.
		if i < 0:
			obj.right(abs(i))
		else:
			obj.left(i)
			'''
		obj.left(i)
		obj.forward(100)
		heading+=i
	print('pirate\'s heading is ', heading % 360, 'counter-clockwise.')
'''
3.8.8
Enhance your program above to also tell us what the drunk pirate’s heading is after he has finished stumbling around. (Assume he begins at heading 0).

'''

drunkenpath(pirate)

wn.mainloop()