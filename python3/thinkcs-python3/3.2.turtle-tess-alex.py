#!/usr/bin/env python

import turtle
wn = turtle.Screen()
wn.bgcolor("DarkTurquoise")
wn.title("Alex and Tess AND RICKY")

alex = turtle.Turtle()

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)

ricky = turtle.Turtle()

def moving_tess(turtle1):	#modification, consolidated the below movements into a def. Now i can assign objects to movements.
	turtle1.penup()
	turtle1.right(90)
	turtle1.forward(80)
	turtle1.pendown()

	colors = ["dark slate grey", "dark salmon", "dark violet"]
	turtle1.shape("classic")

	for i in colors:
		turtle1.color(i)
		turtle1.forward(80)
		turtle1.left(120)

	turtle1.penup()
	turtle1.right(180)
	turtle1.forward(80)
	turtle1.pendown()

def moving_alex(turtle2):	#modification, consolidated the below movements into a def. Now i can assign objects to movements.
	turtle2.shape("turtle")
	for i in ['red', 'white','blue', 'gold']:
		alex.color(i)
		turtle2.forward(50)
		turtle2.left(90)

def moving_ricky(turtle3):
	turtle3.shape("circle")
	turtle3.penup()
	turtle3.left(90)
	turtle3.forward(180)
	turtle3.pensize(20) #set turtle size to 20

	distance = 0

	for i in range(30):
		turtle3.stamp() #leave an impression, remember, the penup() function must be called first.
		distance += 1 	# Increase the size on every iteration
		turtle3.forward(distance) #move ricky forward, the more ricky move, the further each time he does it, the further he moves each time, the faster he is. wahahahh
		turtle3.speed(distance) #speed ricky up!!!
		turtle3.right(24)	#turn ricky 24degrees clockwise each time!

moving_tess(tess)		#try moving_tess(alex), by assigning a turtle object to the def, i can tell it to go a predefined route.
moving_alex(alex)		#try moving_tess(alex), by assigning a turtle object to the def, i can tell it to go a predefined route.
moving_ricky(ricky)
###modification### #here i can tell it to make a certain number of passes through a predefined route! XD
'''
count = 0
while count < 5:
	moving_tess(tess)
	count+=1

counter = 0
while counter < 5:
	moving_tess(alex)
	counter+=1
'''
wn.mainloop()

#there are alot of things to play with, eg changing tess' color for each pass. XD