'''
10.6.4
Now that you’ve got a traffic light program with different turtles for each light, perhaps the visibility / invisibility trick wasn’t such a great idea. If we watch traffic lights, they turn on and off — but when they’re off they are still there, perhaps just a darker color. Modify the program now so that the lights don’t disappear: they are either on, or off. But when they’re off, they’re still visible.
'''
import turtle           # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
#wn.title("Tess becomes a traffic light!")
wn.title("Traffic light!")
wn.bgcolor("gold")
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

    mambo.penup()

draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("light green")
tess.pendown()
#tess.hideturtle()

# Position alex onto the place where the orange light should be
alex.forward(40)
alex.left(90)
alex.forward(120)
# Turn alex into a big orange circle
alex.shape("circle")
alex.shapesize(3)
alex.fillcolor("dark orange")
alex.pendown()
#alex.hideturtle()

# Position mambo onto the place where the red light should be
mambo.forward(40)
mambo.left(90)
mambo.forward(190)
# Turn mambo into a big red circle
mambo.shape("circle")
mambo.shapesize(3)
mambo.fillcolor("dark red")
mambo.pendown()
#mambo.hideturtle()

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        tess.fillcolor("dark green")
        alex.fillcolor("gold")
        #mambo.fillcolor("dark red")
        #tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:     # Transition from state 1 to state 2
        #tess.fillcolor("dark green")
        alex.fillcolor("dark orange")
        mambo.fillcolor("pink")
        state_num = 2
    else:                    # Transition from state 2 to state 0
        #alex.fillcolor("dark orange")
        mambo.fillcolor("dark red")
        tess.fillcolor("light green")
        state_num = 0

# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")

wn.listen()                      # Listen for events
wn.mainloop()