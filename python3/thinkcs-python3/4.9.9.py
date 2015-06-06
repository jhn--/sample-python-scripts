'''
Write a void function to draw a star, where the length of each side is 100 units. (Hint: You should turn the turtle by 144 degrees at each point.)

'''

#! /usr/bin/env python

import turtle

def create_screen(sccolor, sctitle):
    wn = turtle.Screen()
    wn.bgcolor(sccolor)
    wn.title(sctitle)
    return wn

def make_mainloop(wn):
    wn.mainloop()

def draw_star(t, sz):
    for i in range(5):
        t.forward(sz)
        t.right(144)

def makepointer(pcolor, psize):
    t = turtle.Turtle()
    t.color(pcolor)
    t.pensize(psize)
    t.speed(0)
    return t


screen = create_screen("black", "THIS IS A STAR!")
sparta = makepointer("gold", 2)
draw_star(sparta, 100)

make_mainloop(screen)
