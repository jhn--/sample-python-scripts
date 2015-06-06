'''
Write a function which is given an exam mark, and it returns a string — the grade for that mark — according to this scheme:

Mark    Grade
>= 75   First
[70-75) Upper Second
[60-70) Second
[50-60) Third
[45-50) F1 Supp
[40-45) F2
< 40    F3

The square and round brackets denote closed and open intervals. A closed interval includes the number, and open interval excludes it. So 39.99999 gets grade F3, but 40 gets grade F2. Assume

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
Test your function by printing the mark and the grade for all the elements in this list.
'''

#! /usr/bin/env python

def convertmarktograde(listofgrades):
    for i in listofgrades:
        if i >= 75:
            print("Mark", i, "gets Grade - First.")
        elif i >= 70 and i < 75:
            print("Mark", i, "gets Grade - Upper Second.")
        elif i >= 60 and i < 70:
            print("Mark", i, "gets grade - Second.")
        elif i >= 50 and i < 60:
            print("Mark", i, "gets grade - Third.")
        elif i >= 45 and i < 50:
            print("Mark", i, "gets grade - F1 Supp.")
        elif i >= 40 and i < 45:
            print("Mark", i, "gets grade - F2.")
        else:
            print("Mark", i, "gets grade - F3.")

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

convertmarktograde(xs)