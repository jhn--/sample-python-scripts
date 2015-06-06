#! /usr/bin/env python

import turtle

def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("wn blahblahblah whatever")

alex = turtle.Turtle()
draw_square(alex, 50)
wn.mainloop()