'''
Write a function slope(x1, y1, x2, y2) that returns the slope of the line through the points (x1, y1) and (x2, y2). Be sure your implementation of slope can pass the following tests:

test(slope(5, 3, 4, 2) == 1.0)
test(slope(1, 2, 3, 2) == 0.0)
test(slope(1, 2, 3, 3) == 0.5)
test(slope(2, 4, 1, 2) == 2.0)
Then use a call to slope in a new function named intercept(x1, y1, x2, y2) that returns the y-intercept of the line through the points (x1, y1) and (x2, y2)
test(intercept(1, 6, 3, 12) == 3.0)
test(intercept(6, 1, 1, 6) == 7.0)
test(intercept(4, 6, 12, 8) == 5.0)
'''

#! /usr/bin/env python

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno     # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)

def slope(x1, y1, x2, y2):
    '''
    formula for slope = (y2 - y1)/(x2 - x1)
    '''
    xdiff = x2 - x1
    ydiff = y2 - y1
    if ydiff == 0:
        return 0
    else:
        slope = ydiff/xdiff
    #print(slope)
    return slope

def intercept(x1, y1, x2, y2):
    '''
    formula for y-intercept
    y = mx + b
    y-coordinate = (slope * x-coordinate) + y-intercept
    y-intercept = y-coordinate - (slope * x-coordinate)
    '''
    y_int = y1 - (slope(x1, y1, x2, y2) * x1)
    #print(y_int)
    return y_int


test_suite()