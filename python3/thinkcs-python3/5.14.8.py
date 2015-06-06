'''
Modify the turtle bar chart program so that the bar for any value of 200 or more is filled with red, values between [100 and 200) are filled with yellow, and bars representing values less than 100 are filled with green.
'''
'''
In the turtle bar chart program, what do you expect to happen if one or more of the data values in the list is negative? Try it out. Change the program so that when it prints the text value for the negative bars, it puts the text below the bottom of the bar.
'''
#! /usr/bin/env python

import turtle

def draw_screen(scolor, stitle):
    wn = turtle.Screen()
    wn.bgcolor(scolor)
    wn.title(stitle)
    return wn

def create_turtle(tbcolor, tfcolor, tsize, tspeed):
    t = turtle.Turtle()
    t.color(tbcolor, tfcolor)
    t.pensize(tsize)
    t.speed(tspeed)
    return t

def keepwindowopen(t):
    t.mainloop()

def draw_graph(t, height):
    t.left(90)
    t.forward(height)
    t.right(90)
    t.write("  " + str(height))
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.penup()
    t.forward(5)
    t.pendown()

def draw_allthegraphs(t, xs):
    t.penup()
    t.forward(-200)
    t.pendown()
    for i in xs:
        if i >= 200:
            t.color("white", "red")     # can't believe this works
            t.begin_fill()              # can't believe this works too.
            draw_graph(t, i)
            t.end_fill()                # i'm third time lucky.
        elif i >= 100 and i < 200:
            t.color("white", "yellow")
            t.begin_fill()
            draw_graph(t, i)
            t.end_fill()
        elif i >= 0 and i < 100:
            t.color("white", "green")
            t.begin_fill()
            draw_graph(t, i)
            t.end_fill()
        else:
            draw_negative(t, i)

def draw_negative(t, height):
    t.left(90)
    t.forward(height)
    t.penup()              #}
    t.forward(-10)         #} 
    t.write(str(height)    #} Goes further down to print out the value.
    t.forward(10)          #}
    t.pendown()            #} the rest of the code are the same as draw_graph()
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.penup()
    t.forward(5)
    t.pendown()
'''
def draw_negative(t, height): #this doesn't draw graph, it prints out the negative values and draw a straight line.
    t.right(90)
    t.forward(abs(height))
    t.write("  ", str(height))
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(abs(height))
    t.right(90)
    t.penup()
    t.forward(5)
    t.pendown()
'''

xs = [48, 117, 200, 240, 160, 260, 220, -20, -50, -100]

paper = draw_screen("sky blue", "nice bar graph")
tim = create_turtle("white", "red", 2, 0)

draw_allthegraphs(tim, xs)

keepwindowopen(paper)