#! /usr/bin/env python

'''
Write a fruitful function sum_to(n) that returns the sum of all integer numbers up to and including n. So sum_to(10) would be 1+2+3...+10 which would return the value 55.
'''

def sum_to(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

print(sum_to(10))