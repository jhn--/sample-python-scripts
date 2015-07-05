'''
9.6.1
We’ve said nothing in this chapter about whether you can pass tuples as arguments to a function. Construct a small Python example to test whether this is possible, and write up your findings.
'''

import math

a = (1,2,3,4,5)
b = (1,2,3,4,5)

def multiplcation_table(x,y):
    layout = "{0:>4}{1:>4}{2:>4}{3:>4}{4:>4}"
    for i in x:
        print(layout.format(i*y[0], i*y[1], i*y[2], i*y[3], i*y[4]))

multiplcation_table(a,b)