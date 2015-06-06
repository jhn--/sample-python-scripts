'''
10.6.5
Your traffic light controller program has been patented, and you’re about to become seriously rich. But your new client needs a change. They want four states in their state machine: Green, then Green and Orange together, then Orange only, and then Red. Additionally, they want different times spent in each state. The machine should spend 3 seconds in the Green state, followed by one second in the Green+Orange state, then one second in the Orange state, and then 2 seconds in the Red state. Change the logic in the state machine.
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

# Position alex onto the place where the orange light should be
alex.forward(40)
alex.left(90)
alex.forward(120)
# Turn alex into a big orange circle
alex.shape("circle")
alex.shapesize(3)
alex.fillcolor("dark orange")
alex.pendown()

# Position mambo onto the place where the red light should be
mambo.forward(40)
mambo.left(90)
mambo.forward(190)
# Turn mambo into a big red circle
mambo.shape("circle")
mambo.shapesize(3)
mambo.fillcolor("dark red")
mambo.pendown()

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        tess.fillcolor("light green")
        alex.fillcolor("gold")
        #mambo.fillcolor("dark red")
        state_num = 1
        wn.ontimer(advance_state_machine, 1000)
    elif state_num == 1:     # Transition from state 1 to state 2
        tess.fillcolor("dark green")
        alex.fillcolor("gold")
        #mambo.fillcolor("dark red")
        state_num = 2
        wn.ontimer(advance_state_machine, 1000)
    elif state_num == 2:    # Transition from state 2 to state 3
        #tess.fillcolor("dark green")
        alex.fillcolor("dark orange")
        mambo.fillcolor("pink")
        state_num = 3
        wn.ontimer(advance_state_machine, 2000)
    else:                    # Transition from state 2 to state 0
        tess.fillcolor("light green")
        #alex.fillcolor("dark orange")
        mambo.fillcolor("dark red")
        state_num = 0
        wn.ontimer(advance_state_machine, 3000)

# Bind the event handler to the space key.
#wn.onkey(advance_state_machine, "space")
#wn.ontimer(advance_state_machine, 3000)
wn.ontimer(advance_state_machine)

wn.listen()                      # Listen for events
wn.mainloop()