import unittest

from Euler32 import isPandigitalProduct

class Euler32TestCase(unittest.TestCase):
    """Tests for Euler32 functions"""
    def test_isPandigitalProduct(self):
        self.assertEqual(isPandigitalProduct(7254),True)
        self.assertEqual(isPandigitalProduct(7255),False)
        self.assertEqual(isPandigitalProduct(7256),False)

if __name__ == '__main__':
    unittest.main()