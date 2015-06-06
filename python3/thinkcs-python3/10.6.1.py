'''
10.6.1
Add some new key bindings to the first sample program:

Pressing keys R, G or B should change tess’ color to Red, Green or Blue.
Pressing keys + or - should increase or decrease the width of tess’ pen. Ensure that the pen size stays between 1 and 20 (inclusive).
Handle some other keys to change some attributes of tess, or attributes of the window, or to give her new behaviour that can be controlled from the keyboard.
'''

import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle
x = 0
tess.pensize(x)

# The next four functions are our "event handlers".
def h1():
   tess.forward(30)

def h2():
   tess.left(45)

def h3():
   tess.right(45)

def h4():
    wn.bye()                        # Close down the turtle window

def c1():
    tess.color("red")

def c2():
    tess.color("green")

def c3():
    tess.color("blue")

def upsize():
    global x
#    while x < 21:
    if x == 21:
        x = 21
    else:
        x += 1
        wn.title("tess size is {0}".format(x))
    tess.pensize(x)

def downsize():
    global x
#    while x > 0:
    if x == 0:
        x = 0
    else:
        x -= 1
        wn.title("tess size is {0}".format(x))
    tess.pensize(x)

# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

wn.onkey(c1, "r")
wn.onkey(c2, "g")
wn.onkey(c3, "b")

wn.onkey(upsize, "=")
wn.onkey(downsize, "-")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()