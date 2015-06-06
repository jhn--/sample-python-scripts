'''
Extend your program above. Draw five stars, but between each, pick up the pen, move forward by 350 units, turn right by 144, put the pen down, and draw the next star. You’ll get something like this:

http://openbookproject.net/thinkcs/python/english3e/_images/five_stars.png
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

def draw_5stars(t, sz):
    for i in range(5):
        draw_star(t, sz)
        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()

def draw_star(t, sz):
    for i in range(5):
        t.forward(sz)
        t.right(144)

def makepointer(pcolor, psize):
    t = turtle.Turtle()
    t.color(pcolor)
    t.pensize(psize)
    #t.speed(0)
    return t


screen = create_screen("black", "THIS IS A STAR!")
star = makepointer("gold", 2)
draw_5stars(star, 100)

make_mainloop(screen)
