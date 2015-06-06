'''
Write a function days_in_month which takes the name of a month, and returns the number of days in the month. Ignore leap years:

test(days_in_month("February") == 28)
test(days_in_month("December") == 31)
If the function is given invalid arguments, it should return None.
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
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    test(days_in_month("April") == 30)
    test(days_in_month(1) == None)
    test(days_in_month("hello!") == None)

def days_in_month(month):
    month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_num = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in month_name:
        if month == i:
            return month_num[month_name.index(i)]
    return None

test_suite()