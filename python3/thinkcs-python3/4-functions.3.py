#! /usr/bin/env python

import turtle

def draw_multicolor_square(t, sz):
    draw_multicolor_rectangle(t, sz, sz)

def draw_multicolor_rectangle(t, l, w):
    for i in ['green', 'black']:
        t.color(i)
        t.forward(l)
        t.left(90)
        t.forward(w)
        t.left(90)

#    for i in ['red', 'blue', 'hotpink', 'yellow']:
#        t.color(i)
#        t.forward(sz)
#        t.left(90)

wn = turtle.Screen()
wn.bgcolor("gold")

alex = turtle.Turtle()
alex.pensize(3)

size = 20
for i in range(15):
    draw_multicolor_square(alex, size)
    size += 18
    alex.forward(10)
    alex.right(18)

wn.mainloop()