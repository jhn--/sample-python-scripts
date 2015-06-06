#! /usr/bin/env pyhon

import turtle

def create_turtle(tcolor, tsize):
    t = turtle.Turtle()
    t.color(tcolor)
    t.pensize(tsize)
    return t
    '''
    it is import to return the turtle object, t, so that it can be passed to other functions.
    if 'return t' line is ommitted, the error will be 
    AttributeError: 'NoneType' object has no attribute 'forward'
    '''

def draw_queue(t, distance):
    for i in range(5):
        draw_square(t, distance) 
        '''
        pass the turtle obj, alex, as a parameter, dont call the draw_square() function as if its an attribute of the object.
        eg. t.draw_square(distance) 
        will return error:
        AttributeError: 'Turtle' object has no attribute 'draw_square'
        '''
        t.penup()
        t.forward(distance*2)
        t.pendown()

def draw_square(t, distance):
    for i in range(4):
        t.forward(distance)
        t.left(90)

def create_screen(sccolor, sctitle):
    wn = turtle.Screen()
    wn.bgcolor(sccolor)
    wn.title(sctitle)
    return wn
    '''
    return wn so that it can be used in make_mainloop function to call mainloop()
    the variable "screen", will be assigned the value, wn, when create_screen() returns wn.
    '''

def make_mainloop(wn):
    wn.mainloop()

screen = create_screen("dark grey", "Ninja Turtles!")

alex = create_turtle("hotpink", 1)
draw_queue(alex, 20)

make_mainloop(screen)
