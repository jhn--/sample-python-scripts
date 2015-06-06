#! /usr/bin/env python

import turtle
wn = turtle.Screen()
wn_color = input('''What color will you like for your canvas? 
	E.g. red, green, blue or even cornsilk!
	See http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm for more options: ''')

try:
	wn.bgcolor(wn_color)
except:
	print("I think there's a problem with the color you chose, please try again.")
	#break

wn.title("Hello, tess!")		#set the window title

tess = turtle.Turtle()

turtle_color = input('''What color will you like for your turtle? 
	E.g. Same as the colors for your canvas; red, green, blue or even cornsilk!
	See http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm for more options: ''')
try:
	tess.color(turtle_color)				#tell tess to change her color
except:
	print('''Hrmmmmm... there's been an error somewhere, maybe the color doesn't exist.
		Please try again!''')
	#break

turtle_pensize = input('''Last question, how big will you like your turtle?
	You can choose whatever size you want but make sure it is not negative.
	And not too big, or else it is going to look funny. XD
	Size 1 to 10 ought to be enough!''')

try:
	tess.pensize(int(turtle_pensize))					#tell tess to change her pen width
except:
	print("Oh man, another error has occured. I'm out of here!")

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()