'''
This works, from http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html.
'''
import math

def binarysearch(input, target):
    input.sort()
    start_index = 0
    end_index = len(input) - 1
    found = False

    while start_index < end_index and not found:
        mid_index = math.floor((start_index + end_index) / 2)
        if input[mid_index] == target:
            found = True
        else:
            if input[mid_index] < target:
                start_index = mid_index + 1
            else:
                end_index = mid_index - 1

    return found

print(binarysearch([1,2,3,4,5,6,7,8,9,10], 8))
print(binarysearch([1,2,3,4,5,6,7,8,9,10], 3))
print(binarysearch([1,2,3,4,5,6,7,8,9,10], 11))
print(binarysearch([1,2,45,90,32,9,10], 11)) #stuck here. 


'''
From http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html, this works too.
'''
def search_binary(xs, target):
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:
           return -1

        mid_index = (lb + ub) // 2

        item_at_mid = xs[mid_index]

        if item_at_mid == target:
            return mid_index
        if item_at_mid < target:
            lb = mid_index + 1
        else:
            ub = mid_index

'''
Here we have another example, taken from http://algorithms.openmymind.net/search/binarysearch.html which shows recursive calling of the same function, which I think is a lot cooler. But it doesn't _work_. =/
'''

import math

def findtarget(input, target):
    input.sort()
    return binarysearch(input, target, start = 0, end = len(input) - 1)

def binarysearch(input, target, start, end):
    if (end < start):
        return "Value: {0} doesn't exit.".format(target)
    else:
        mid = math.floor((start + end) / 2)
        value = input[mid]
        if (value > target):
            binarysearch(input, target, start, mid - 1)
        if (value < target):
            binarysearch(input, target, mid + 1, end)
    return mid
        

print(findtarget([1,2,3,4,5,6,7,8,9,10], 8))
print(findtarget([1,2,3,4,5,6,7,8,9,10], 3))
print(findtarget([1,2,3,4,5,6,7,8,9,10], 11))
print(findtarget([1,2,45,90,32,9,10], 11)) #stuck here.