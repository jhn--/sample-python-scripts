#! /usr/bin/env python

import turtle
import math

def draw_bigger_squares(t, distance):
    margin = math.sqrt(((distance/2)**2)+((distance/2)**2))
    for i in range(6):
        draw_square(t, distance)
        t.right(135)
        t.penup()
        t.forward(margin)
        t.left(135)
        t.pendown()
        distance += 20

def draw_square(t, distance):
    for i in range(4):
        t.forward(distance)
        t.left(90)

def create_turtle(tcolor, tsize):
    t = turtle.Turtle()
    t.color(tcolor)
    t.pensize(tsize)
    return t

def create_screen(sccolor, sctitle):
    wn = turtle.Screen()
    wn.bgcolor(sccolor)
    wn.title(sctitle)
    return wn

def make_mainloop(wn):
    wn.mainloop()

screen = create_screen("black", "Ninja Turtles!")

alex = create_turtle("gold", 1)
draw_bigger_squares(alex, 20)

make_mainloop(screen)
