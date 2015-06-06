'''
Write a function day_name that converts an integer number 0 to 6 into the name of a day. Assume day 0 is “Sunday”. Once again, return None if the arguments to the function are not valid. Here are some tests that should pass:

test(day_name(3) == "Wednesday")
test(day_name(6) == "Saturday")
test(day_name(42) == None)
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
    test(day_name(0) == "Sunday")
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)

def day_name(day):
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    '''
    #this is so wrong, what happens is when running day_name(3), when 3 is being matched with i, which is 0, and doesn't match, it returns None. That's wrong.
    for i in range(len(week)):
        if day == i:
            return week[day]
        else:
            return None
    '''
    '''
    #this is slightly better but according to the folks at #python, the for loop is still pointless........ i was gonna use a forloop to cut away the multiple meaningless lines of if:elif:else choices but there is a better choice.
    #anyway, but removing the "else: return None" condition, anything thats not in the for loop will proceed out and return None.
    for i in range(len(week)):
        if day == i:
            return week[day]
    return None
    '''
    '''
    #now, this is the best approach to solving the problem!
    #since day ought to be between 0 and 6, 'if 0 <= day < len(week):' will satisfy two conditions necessary to return the name of the day.
    #no for loops needed.
    '''
    if 0 <= day < len(week):
        return week[day]
    else:
        return None

test_suite()



#Yhg1s > empyrean: 
#just do 'if 0 <= day < len(week): return week[day];; return None'

