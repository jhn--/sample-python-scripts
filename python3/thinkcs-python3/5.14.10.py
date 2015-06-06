'''Write a function find_hypot which, given the length of two sides of a right-angled triangle, returns the length of the hypotenuse. (Hint: x ** 0.5 will return the square root.)
'''

#! /usr/bin/env python

import math

def find_hypot(side1, side2):
    hypot = math.sqrt((side1 ** 2) + (side2 ** 2))
    return hypot

print(find_hypot(10, 10))