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
def two_for(arr: list, target: int) -> list:
    '''
    x: int, the current value in the list, arr
    xi: index of x
    z: int, the current value in the list, arr in the second loop
    zi: index of z
    '''
    for (xi, x) in enumerate(arr):
        for (zi, z) in enumerate(arr):
            if xi == zi:
                pass
            if target - x == z:
                return [xi, zi]
    return []

# arr = [2, 7, 11, 15]
# target = 18
# print(two_for(arr, target))