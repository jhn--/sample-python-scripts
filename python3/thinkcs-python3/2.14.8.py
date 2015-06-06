#Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), and ask for the number of hours to wait. Your program should output what the time will be on the clock when the alarm goes off.

#! /usr/bin/env python

gettimefromuser = int(input("What's the time now? please enter in military timing, eg. 1400 hrs etc : "))

howmanyhourstowait = int(input("How many hours to wait before waking you up?: "))

timetowakeup = (gettimefromuser + (howmanyhourstowait*100)) % 2400
print("ok, i will wake you up at",timetowakeup,"hrs.")