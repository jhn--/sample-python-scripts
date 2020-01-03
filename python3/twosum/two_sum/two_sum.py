#!/usr/bin/env python3

# https://leetcode.com/problems/two-sum/

# problem statement
"""
Given an array of integers, return indices of the two numbers 
such that they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
def two_sum(arr: list, target: int) -> list:
    '''
    if y, the result of (target-x), exists in the list (arr)
    return the indexes of both x and y.
    '''

    for x in arr:
        y = target - x
        if y in arr:
            return [arr.index(x), arr.index(y)]
    
    return [-1,-1]

# arr = [2, 7, 11, 15]
# target = 9
# print(two_sum(arr, target))