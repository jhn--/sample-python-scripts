'''
Many interesting shapes can be drawn by the turtle by giving a list of pairs like we did above, where the first item of the pair is the angle to turn, and the second item is the distance to move forward. Set up a list of pairs so that the turtle draws a house with a cross through the centre, as show here. This should be done without going over any of the lines / edges more than once, and without lifting your pen.
http://openbookproject.net/thinkcs/python/english3e/_images/tess_house.png
'''

import turtle

def createScreen():
    wn = turtle.Screen()
    return wn

def createTurtle():
    t = turtle.Turtle()
    return t

def drawHouse(t, house):
    for (i, j) in house:
        t.write(i)
        t.left(i)
        t.forward(j)

wn = createScreen()
t = createTurtle()

house = [(45, 100), (225, 70), (270, 70), (270, 70), (310, 50), (270, 50), (225, 70), (135, 100)]
drawHouse(t, house)

wn.mainloop()