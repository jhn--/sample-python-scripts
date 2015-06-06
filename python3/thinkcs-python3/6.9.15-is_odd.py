'''
Now write the function is_odd(n) that returns True when n is odd and False otherwise. Include unit tests for this function too.

Finally, modify it so that it uses a call to is_even to determine if its argument is an odd integer, and ensure that its test still pass.
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
    test(is_even(2) == False)
    test(is_even(101) == True)
    test(is_even(0) == False)
    test(is_even(1.2) == False)
    test(is_even(1) == True)

def is_odd(n):
    is_even(n)

def is_even(n):
    if n % 2 == 1:
        return True
    return False

test_suite()