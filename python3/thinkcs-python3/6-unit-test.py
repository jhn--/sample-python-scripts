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
    '''
    Run the suite of tests for code in this module (this file).
    '''
    test(abs_value(17) == 17)
    test(abs_value(-17) == 17)
    test(abs_value(0) == 0)
    test(abs_value(3.14) == 3.14)
    test(abs_value(-3.14) == 3.14)

def abs_value(x):
    if x < 0:
        return (x * -1)
    return x

'''
def abs_value(x):    #buggy version
    if x < 0:
        return 1
    elif x > 0:
        return x
'''

test_suite()