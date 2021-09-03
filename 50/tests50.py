import unittest

import euler50

class Euler50_tests(unittest.TestCase):
    """Tests for euler #50"""

    def test_consecutivePrimeSums(self):
        self.assertEqual(euler50.consecutivePrimeSums(6,100),[41])
        self.assertEqual(euler50.consecutivePrimeSums(21,1000),[953])

if __name__ == '__main__':
    unittest.main()