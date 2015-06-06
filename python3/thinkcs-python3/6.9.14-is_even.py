'''
Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number and False if it is odd.

Add your own tests to the test suite.
'''

#! /usr/bin/env python

import sys, math

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno     # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    test(is_even(2) == True)
    test(is_even(101) == False)
    test(is_even(0) == True)
    test(is_even(1.2) == False)
    test(is_even(1) == False)

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    return None

test_suite()