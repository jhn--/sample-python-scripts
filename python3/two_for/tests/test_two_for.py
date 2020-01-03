import unittest

from two_for import two_for

class TestTwoFor(unittest.TestCase):
    def test_two_for(self):
        """
        
        """
        arr = [2, 7, 11, 15]
        target = 9
        result = two_for(arr, target)
        self.assertEqual(result, [0,1])

if __name__ == '__main__':
    unittest.main()