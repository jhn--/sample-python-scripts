'''
Can your day_add function already work with negative deltas? For example, -1 would be yesterday, or -7 would be a week ago:

test(day_add("Sunday", -1) == "Saturday")
test(day_add("Sunday", -7) == "Sunday")
test(day_add("Tuesday", -100) == "Sunday")
If your function already works, explain why. If it does not work, make it work.

Hint: Play with some cases of using the modulus function % (introduced at the beginning of the previous chapter). Specifically, explore what happens to x % 7 when x is negative.
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
    '''
    Run the suite of tests for code in this module (this file).
    '''
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")

def day_num(daynum):
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for i in week:
        if daynum == i:
            return week.index(daynum)
    return None

def day_name(dayname):
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if 0 <= dayname < len(week):
        return week[dayname]
    else:
        return None

def day_add(startday, delta):
    '''
    Same code as 6.9.4-day_add.py, works with negative deltas.
    '''
    return day_name((day_num(startday) + delta) % 7)

test_suite()
