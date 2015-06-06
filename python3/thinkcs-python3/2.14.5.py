#The formula for computing the final amount if one is earning compound interest is given on Wikipedia as
#http://openbookproject.net/thinkcs/python/english3e/_images/compoundInterest.png
#Write a Python program that assigns the principal amount of $10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8%. Then have the program prompt the user for the number of years t that the money will be compounded for. Calculate and print the final amount after t years.

#! /usr/bin/env python

P = 10000
n = 12
r = 0.08

t = int(input("Enter the number of years: "))

for i in (range(1,t+1)):
	A = P * ((1 + (r/n))**(n*i))
	print("compound interest for year", i, ": ", A)