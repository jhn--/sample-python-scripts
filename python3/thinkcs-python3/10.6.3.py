'''
10.6.3
In an earlier chapter we saw two turtle methods, hideturtle and showturtle that can hide or show a turtle. This suggests that we could take a different approach to the traffic lights program. Add to your program above as follows: draw a second housing for another set of traffic lights. Create three separate turtles to represent each of the green, orange and red lights, and position them appropriately within your new housing. As your state changes occur, just make one of the three turtles visible at any time. Once you’ve made the changes, sit back and ponder some deep thoughts: you’ve now got two different ways to use turtles to simulate the traffic lights, and both seem to work. Is one approach somehow preferable to the other? Which one more closely resembles reality — i.e. the traffic lights in your town?
'''
import turtle           # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
#wn.title("Tess becomes a traffic light!")
wn.title("Traffic light!")
wn.bgcolor("pink")
tess = turtle.Turtle()
alex = turtle.Turtle()
mambo = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

    alex.penup()
    '''
    alex.pensize(3)
    alex.color("black", "darkgrey")
    #alex.begin_fill()
    alex.forward(80)
    alex.left(90)
    alex.forward(200)
    alex.circle(40, 180)
    alex.forward(200)
    alex.left(90)
    #alex.end_fill()'''

    mambo.penup()
    '''
    mambo.pensize(3)
    mambo.color("black", "darkgrey")
    #mambo.begin_fill()
    mambo.forward(80)
    mambo.left(90)
    mambo.forward(200)
    mambo.circle(40, 180)
    mambo.forward(200)
    mambo.left(90)
    #mambo.end_fill()
'''
draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")
tess.pendown()
#tess.hideturtle()

# Position alex onto the place where the orange light should be
alex.forward(40)
alex.left(90)
alex.forward(120)
# Turn alex into a big orange circle
alex.shape("circle")
alex.shapesize(3)
alex.fillcolor("orange")
alex.pendown()
alex.hideturtle()

# Position mambo onto the place where the red light should be
mambo.forward(40)
mambo.left(90)
mambo.forward(190)
# Turn mambo into a big red circle
mambo.shape("circle")
mambo.shapesize(3)
mambo.fillcolor("red")
mambo.pendown()
mambo.hideturtle()

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        tess.hideturtle()
        alex.showturtle()
        mambo.hideturtle()
        #tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:     # Transition from state 1 to state 2
        tess.hideturtle()
        alex.hideturtle()
        mambo.showturtle()
        #tess.fillcolor("red")
        state_num = 2
    else:                    # Transition from state 2 to state 0
        tess.showturtle()
        alex.hideturtle()
        mambo.hideturtle()
        #tess.back(140)
        #tess.fillcolor("green")
        state_num = 0

# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")

wn.listen()                      # Listen for events
wn.mainloop()