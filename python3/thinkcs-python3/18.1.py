import turtle

wn = turtle.Screen()
pichu = turtle.Turtle()

pichu.penup()
pichu.forward(-300)
pichu.pendown()
pichu.speed(1)

def koch(t, order, size):
    """
    koch
    """
    if order == 0:
        t.forward(size)
    else:
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)

def koch2(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for i in [60, -120, 60, 0]:
            print("order is now {0}, drawing {1}, turning angle {2}.".format(order, size, i))
            koch2(t, order-1, size/3)
            t.left(i)

#koch(pichu, 0, 120)

koch2(pichu, 4, 600)

wn.mainloop()

