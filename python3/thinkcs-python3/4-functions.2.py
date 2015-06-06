#! /usr/bin/env python

import turtle

def draw_multicolor_square(t, sz):
    for i in ['red', 'blue', 'hotpink', 'yellow']:
        t.color(i)
        t.forward(sz)
        t.turn(90)

wn = turtle.Screen()
wn.bgcolor("black")

alex = turtle.Turtle()
alex.pensize(3)

size = 20
for i in range(15):
    draw_multicolor_square(alex, size)
    size += 18
    alex.forward(10)
    alex.right(18)

wn.mainloop()