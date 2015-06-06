'''
Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):

An equilateral triangle
A square
A hexagon (six sides)
An octagon (eight sides)
'''

#! /usr/bin/env python

import turtle
wn = turtle.Screen()
pointer = turtle.Turtle()

def draw_equi_tri(obj):
	for i in range(3):
		obj.forward(20)
		obj.left(120)

def draw_square(obj):
	for i in range(4):
		obj.forward(20)
		obj.left(90)

def draw_hex(obj):
	for i in range(6):
		obj.forward(20)
		obj.left(60)

def draw_oct(obj):
	for i in range(8):
		obj.forward(20)
		obj.left(45)

draw_equi_tri(pointer)
draw_square(pointer)
draw_hex(pointer)
draw_oct(pointer)

wn.mainloop()