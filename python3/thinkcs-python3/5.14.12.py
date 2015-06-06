'''Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.

Hint: Floating point arithmetic is not always exactly accurate, so it is not safe to test floating point numbers for equality. If a good programmer wants to know whether x is equal or close enough to y, they would probably code it up as:

    if  abs(x-y) < 0.000001:    # If x is approximately equal to y...
'''
'''
Extend the above program so that the sides can be given to the function in any order.
'''

#! /usr/bin/env python

def is_rightangled(side1, side2, longest):
    side1sq = side1 ** 2
    side2sq = side2 ** 2
    sumo = side1sq + side2sq
    longestsq = longest ** 2
    print("#################################")
    print("side1: ", side1, "^2 =", side1sq)
    print("side2: ", side2, "^2 =", side2sq)
    print("Sum of ", side1, "^2 and ", side2, "^2 is", sumo)
    print("longest side, the probable hypoteneuse", longest, "^2 =", longestsq)
    print("Any difference less than 0.0001 is counted as 0.")
    if abs(((side1 ** 2) + (side2 ** 2)) - (longest ** 2)) < 0.05:
        print("yeah right-angled triangle")
    else:
        print("naw man, not right-angled triangle")
    print("#################################")

def findlongest(xs):
    if xs[0] > xs[1] and xs[0] > 2:
        side1 = xs[1]
        side2 = xs[2]
        longest = xs[0]
    elif xs[1] > xs[0] and xs[1] > xs[2]:
        side1 = xs[0]
        side2 = xs[2]
        longest = xs[1]
    else:
        side1 = xs[0]
        side2 = xs[1]
        longest = xs[2]
    is_rightangled(side1, side2, longest)

'''
is_rightangled(3,4,5)
is_rightangled(1.1,2,2.1)
is_rightangled(7.5, 8.2, 11.04)
is_rightangled(7.5, 8.1, 11.03902)
is_rightangled(6.9, 9.9, 12.069)
'''
listofsides = [3,4,5]
findlongest(listofsides)