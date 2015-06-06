'''
Write three functions that are the “inverses” of to_secs:

hours_in returns the whole integer number of hours represented by a total number of seconds.
minutes_in returns the whole integer number of left over minutes in a total number of seconds, once the hours have been taken out.
seconds_in returns the left over seconds represented by a total number of seconds.
You may assume that the total number of seconds passed to these functions is an integer. Here are some test cases:

test(hours_in(9010) == 2)
test(minutes_in(9010) == 30)
test(seconds_in(9010) == 10)
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
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)

def hours_in(x):
    hours = x // 3600
    return hours

def minutes_in(x):
    minutes = (x % 3600) // 60
    return minutes

def seconds_in(x):
    seconds = (x % 3600) % 60
    return seconds

test_suite()