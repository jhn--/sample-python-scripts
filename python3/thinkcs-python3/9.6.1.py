'''
9.6.1
We’ve said nothing in this chapter about whether you can pass tuples as arguments to a function. Construct a small Python example to test whether this is possible, and write up your findings.
'''

import math

a = (1,2,3,4,5)
b = (1,2,3,4,5)

def multiplcation_table(x,y):
    layout = "{0:>4}{1:>4}{2:>4}{3:>4}{4:>4}"
    for i in a:
#        print(layout.format(i*j))
        print(layout.format(i*b[0], i*b[1], i*b[2], i*b[3], i*b[4]))
#        print(layout.format(i*j))

multiplcation_table(a,b)