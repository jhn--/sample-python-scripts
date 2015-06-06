#!/usr/bin/python

choice = raw_input('Enjoying the course? (y/n)')

while choice.lower() != "y" or choice.lower() != "n":#fill in the condition
    choice = raw_input("Sorry I didn't catch that.  Enter again: ")

