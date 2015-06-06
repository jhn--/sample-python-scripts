'''
Write a program to draw a face of a clock that looks something like this:

http://openbookproject.net/thinkcs/python/english3e/_images/tess_clock1.png
'''

#! /usr/bin/env python

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
u = turtle.Turtle()

wn.bgcolor("gold")

#t.color("blue")
t.pensize(20)
t.shape("turtle")
t.penup()
t.stamp()

#u.color("blue")
u.pensize(5)
u.shape("square")
u.shapesize(0.1,1)
u.penup()

hours = 12

#anglestoturn = 180 - ((180 * (12 - 2))/hours)
anglestoturn = 360 / hours
#distancebetweenhrs = (2 * 3.14 * 100) / 12

for i in range(hours):
	u.forward(80)
	t.forward(100)
	t.stamp()
	u.stamp()
	u.forward(-80)
	t.forward(-100)
	t.right(anglestoturn)
	u.right(anglestoturn)

wn.mainloop()