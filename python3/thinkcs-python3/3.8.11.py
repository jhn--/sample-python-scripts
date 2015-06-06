'''
Write a program to draw a shape like this:

http://openbookproject.net/thinkcs/python/english3e/_images/star.png

Hints:

Try this on a piece of paper, moving and turning your cellphone as if it was a turtle. Watch how many complete rotations your cellphone makes before you complete the star. Since each full rotation is 360 degrees, you can figure out the total number of degrees that your phone was rotated through. If you divide that by 5, because there are five points to the star, you’ll know how many degrees to turn the turtle at each point.
You can hide a turtle behind its invisibility cloak if you don’t want it shown. It will still draw its lines if its pen is down. The method is invoked as tess.hideturtle() . To make the turtle visible again, use tess.showturtle()
'''
# http://www.algebra.com/algebra/homework/Polygons/Polygons.faq.question.225075.html

#! /usr/bin/env python

import turtle

wn = turtle.Screen()

an_n_pointed_star = int(input("how many points do you want your star to have? BTW, i can't draw anything other than a 5 pointed star. LOL: "))

def angleofnpointedstar(points):
	total_interiorangle = 180 * (points - 2)
	eachinterangle = total_interiorangle / 5
	angleofpoint = 180 - ((180 - eachinterangle) * 2)
	drawstar(points, angleofpoint)

def drawstar(points, angleofpoint):
	t = turtle.Turtle()
	t.hideturtle()
	turningangle = 180 - angleofpoint
	for i in range(points):
		t.forward(50)
		t.right(turningangle)

angleofnpointedstar(an_n_pointed_star)

wn.mainloop()