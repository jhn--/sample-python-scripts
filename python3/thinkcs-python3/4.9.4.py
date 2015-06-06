#! /usr/bin/env python

import turtle

def draw_thisiscrazy(t, distance):
    for i in range(5):
        draw_big_squares(t, distance)
        t.left(18)

def draw_big_squares(t, distance):
    for i in range(4):
        t.left(-90)
        draw_square(t, distance)

def draw_square(t, distance):
    for i in range(4):
        t.forward(distance)
        t.left(90)

def create_turtle(tcolor, tsize):
    t = turtle.Turtle()
    t.color(tcolor)
    t.pensize(tsize)
    t.speed(0)
    return t

def create_screen(sccolor, sctitle):
    wn = turtle.Screen()
    wn.bgcolor(sccolor)
    wn.title(sctitle)
    return wn

def make_mainloop(wn):
    wn.mainloop()

screen = create_screen("black", "Ninja Turtles!")

alex = create_turtle("gold", 3)
draw_thisiscrazy(alex, 80)

make_mainloop(screen)
