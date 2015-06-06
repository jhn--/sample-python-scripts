'''
Revisit the drunk pirate problem from the exercises in chapter 3. This time, the drunk pirate makes a turn, and then takes some steps forward, and repeats this. Our social science student now records pairs of data: the angle of each turn, and the number of steps taken after the turn. Her experimental data is [(160, 20), (-43, 10), (270, 8), (-43, 12)]. Use a turtle to draw the path taken by our drunk friend.
'''

import turtle

def createScreen():
    wn = turtle.Screen()
    return wn

def createTurtle():
    t = turtle.Turtle()
    t.speed(1)
    return t

def drunken_pirate(t, drunken_walk):
    for (i, j) in drunken_walk:
        t.left(i)
        t.forward(j)
        t.write(i, j)

xs = [(160, 20), (-43, 10), (270, 8), (-43, 12)]
wn = createScreen()
t = createTurtle()

drunken_pirate(t, xs)

wn.mainloop()