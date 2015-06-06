'''
Write is_multiple to satisfy these unit tests:

test(is_multiple(12, 3))
test(is_multiple(12, 4))
test(not is_multiple(12, 5))
test(is_multiple(12, 6))
test(not is_multiple(12, 7))
Can you find a way to use is_factor in your definition of is_multiple?
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
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))

'''
def is_multiple(x, y):
    if y == 0:
        print(False)
        return False
    elif x % y == 0:
        return True
    else:
        return False
'''
def is_factor(x, y):
    if x % y == 0:
        return True
    else:
        return False

def is_multiple(x, y):
    if y == 0:
        return False
    else:
        return is_factor(x, y) 
        #i spent like 2-3 hours thinking why the code doesn't work, and i ended up going to irc to look for an answer, only to realise that i need a return before the function.
        #ARGH

test_suite()