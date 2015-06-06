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
    t.forward(10)
    t.pendown()

def keepwindowopen(t):
    t.mainloop()

def draw_allthegraphs(t, xs):
    t.penup()
    t.forward(-200)
    t.pendown()
    for i in xs:
        draw_graph(t, i)

xs = [48, 117, 200, 240, 160, 260, 220]

paper = draw_screen("sky blue", "nice bar graph")
tim = create_turtle("white", "red", 2, 9)

draw_allthegraphs(tim, xs)

keepwindowopen(paper)