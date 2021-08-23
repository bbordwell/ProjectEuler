import unittest

import usefulfunctions

class useful_functions_tests(unittest.TestCase):
    """Tests for usefulfunctions"""

    def test_fibonacci_n(self):
        """Test Fibonacci function using n="""
        self.assertEqual(usefulfunctions.fibonacci(n=10),[1,2,3,5,8,13,21,34,55,89])

    def test_fibonacci_maxValue(self):
        """Test Fibonacci function using maxValue"""
        self.assertEqual(usefulfunctions.fibonacci(maxValue=89),[1,2,3,5,8,13,21,34,55,89])

if __name__ == '__main__':
    unittest.main()