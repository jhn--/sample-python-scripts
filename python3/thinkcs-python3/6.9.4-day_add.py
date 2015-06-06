'''
Write a function that helps answer questions like ‘“Today is Wednesday. I leave on holiday in 19 days time. What day will that be?”’ So the function must take a day name and a delta argument — the number of days to add — and should return the resulting day name:

test(day_add("Monday", 4) ==  "Friday")
test(day_add("Tuesday", 0) == "Tuesday")
test(day_add("Tuesday", 14) == "Tuesday")
test(day_add("Sunday", 100) == "Tuesday")
Hint: use the first two functions written above to help you write this one.
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
    test(day_add("Monday", 4) ==  "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")

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
    return day_name((day_num(startday) + delta) % 7)

test_suite()
