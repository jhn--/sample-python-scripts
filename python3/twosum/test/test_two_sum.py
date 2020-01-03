import unittest

from two_sum.main import ts


class TestTwoSum(unittest.TestCase):
    def two_sum_success(self):
        '''
        two_sum(arr, target) ought to return [0,1]
        '''
        arr1 = [2, 7, 11, 15]
        target1 = 9
        result1 = ts(arr1, target1)
        expected_result1 = [0, 1]
        self.assertEqual(result1, expected_result1)

    def two_sum_fail(self):
        '''
        two_sum(arr, target) ought to return [-1,-1]
        '''
        arr2 = [2, 7, 11, 15]
        target2 = 10
        result2 = ts(arr2, target2)
        expected_result2 = [-1,-1]
        self.assertEqual(result2, expected_result2)


if __name__ == '__main__':
    unittest.main()
