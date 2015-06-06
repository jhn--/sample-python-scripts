'''
Write the inverse function day_num which is given a day name, and returns its number:

test(day_num("Friday") == 5)
test(day_num("Sunday") == 0)
test(day_num(day_name(3)) == 3)
test(day_name(day_num("Thursday")) == "Thursday")
Once again, if this function is given an invalid argument, it should return None:

test(day_num("Halloween") == None)
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
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)

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

test_suite()
