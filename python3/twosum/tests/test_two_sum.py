# import unittest

# import two_sum


# class TestTwoSum(unittest.TestCase):
#     def two_sum_success(self):
#         '''
#         two_sum(arr, target) ought to return [0,1]
#         '''
#         arr = [2, 7, 11, 15]
#         target = 9
#         result = two_sum(arr, target)
#         self.assertEqual(result, [0, 1])

#     def two_sum_fail(self):
#         '''
#         two_sum(arr, target) ought to return [-1,-1]
#         '''
#         arr = [2, 7, 11, 15]
#         target = 10
#         result = two_sum(arr, target)
#         self.assertEqual(result, [-1, -1])


# if __name__ == '__main__':
#     unittest.main()

import pytest

from two_sum import two_sum

def two_sum_success():
    arr = [2, 7, 11, 15]
    target = 9
    assert two_sum(arr, target) == [0,1], 'should be [0,1]'

def two_sum_fail():
    arr = [2, 7, 11, 15]
    target = 10
    assert two_sum(arr, target) == [-1,-1], 'should be [-1,-1]'