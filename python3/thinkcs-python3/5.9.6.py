#! /usr/bin/env python

import turtle

def create_screen(sccolor, sctitle):
    wn = turtle.Screen()
    wn.bgcolor(sccolor)
    wn.title(sctitle)
    return wn

def make_mainloop(wn):
    wn.mainloop()

def draw_poly(t, n, sz):
    sumofinternalangles = 180 * (n - 2)
    internalangle = sumofinternalangles / n
    turningangle = 180 - internalangle
    for i in range(n):
        t.forward(sz)
        t.left(turningangle)

def draw_equitriangle(t, sz):
    draw_poly(t, 3, sz)

def makepointer(pcolor, psize):
    t = turtle.Turtle()
    t.color(pcolor)
    t.pensize(psize)
    t.speed(0)
    return t


screen = create_screen("black", "THIS IS SPARTA!")
sparta = makepointer("gold", 2)
draw_poly(sparta, 8, 50)

make_mainloop(screen)
