'''
Note: What if your application is a single script?

You can import any attributes of the script, such as classes, functions, and variables by using the built-in __import__() function. Instead of from my_sum import sum, you can write the following:

target = __import__("my_sum.py")
sum = target.sum
The benefit of using __import__() is that you don’t have to turn your project folder into a package, and you can specify the file name. This is also useful if your filename collides with any standard library packages. For example, math.py would collide with the math module.
'''

import unittest

from fractions import Fraction
from my_sum import sum
# target = __import__('my_sum.py', globals(), locals(), [], 1)
# sum = target.sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1,4), Fraction(1,4), Fraction(1,2)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()