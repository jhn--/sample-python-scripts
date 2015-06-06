'''
12.2.the_time_module
'''

import time

def do_my_sum(sz):
    total = 0
    for i in sz:
        total += i
    return total

sz = 10000000
testdata = range(sz)

t0 = time.clock()
my_result = do_my_sum(testdata)
t1 = time.clock()
print("my result : {0} (time taken = {1:.4f} seconds)".format(my_result, t1-t0))

t2 = time.clock()
their_result = sum(testdata)
t3 = time.clock()
print("their result : {0} (time taken = {1:.4f} seconds)".format(their_result, t3-t2))