'''
If you were going to draw a regular polygon with 18 sides, what angle would you need to turn the turtle at each corner?
'''

#formula to calculate sum of interior angles in a polygon is 180(n - 2).

#! /usr/bin/env python

import turtle

#sides = 18

sides = int(input("give me the number of sides you want for your polygon, and i will draw it out for you: "))

sumofintangleofpolygon = 180*(sides - 2)

angleofturningleft = 180 - (sumofintangleofpolygon/sides)

print("sum of interior angle of a", sides, "- sided polygon is", sumofintangleofpolygon)

print("angle of turning for is", angleofturningleft, "degrees anti-clockwise.")

wn = turtle.Screen()
pointer = turtle.Turtle()

for i in range(sides):
	pointer.forward(50)
	pointer.left(angleofturningleft)

wn.mainloop()