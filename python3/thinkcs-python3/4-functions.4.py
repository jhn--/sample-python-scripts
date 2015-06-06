#! /usr/bin/env python

import turtle

def make_window(wcolor, wtitle):
    wn = turtle.Screen()
    wn.bgcolor(wcolor)
    wn.title(wtitle)

def make_turtles(tcolor, tsize, polygon_dist, polygon_sides):
    t = turtle.Turtle()
    t.color(tcolor)
    t.pensize(tsize)
    draw_polygon(t, polygon_dist, polygon_sides)

def draw_polygon(tname, polygon_dist, polygon_sides):
    angle = 180 - ((180 * (polygon_sides - 2)) / polygon_sides)
    for i in range(polygon_sides):
        tname.forward(polygon_dist)
        tname.left(angle)

#def create_terrarium(tcolor, tsize, tname):
#    make_turtles(tname, tcolor, tsize)

win = make_window("grey", "turtle terrarium")

alex = make_turtles("yellow", 10, 50, 4)

print(type(win))

#questions
#where do I input the mainloop() command to keep window open?
#how should i call it since its in a function?
