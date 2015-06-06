#! /usr/bin/env python

#! /usr/bin/env python

import turtle

def create_screen(sccolor, sctitle):
    wn = turtle.Screen()
    wn.bgcolor(sccolor)
    wn.title(sctitle)
    return wn

def make_mainloop(wn):
    wn.mainloop()

def this_is_sparta(t, distance):
    for i in range(99):
        t.left(-90)
        t.forward(distance)
        distance += 5
    t.left(-90)

def makepointer(pcolor, psize):
    t = turtle.Turtle()
    t.color(pcolor)
    t.pensize(psize)
    t.speed(0)
    return t


screen = create_screen("black", "THIS IS SPARTA!")
sparta = makepointer("gold", 2)
this_is_sparta(sparta, 10)
make_mainloop(screen)
