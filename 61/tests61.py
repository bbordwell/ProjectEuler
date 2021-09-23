import unittest

import euler61

class Euler61_Tests(unittest.TestCase):
    """Tests for Euler 61"""

    def test_addition(self):
        """Test that simple FigurateNumber addition works."""
        self.assertEqual((euler61.FigurateNumber(8128,'triangle') + euler61.FigurateNumber(2882,'square')).n,'81282882')
        self.assertEqual((euler61.FigurateNumber(8128,'triangle') + euler61.FigurateNumber(2882,'square')).triangle,True)
        self.assertEqual((euler61.FigurateNumber(8128,'triangle') + euler61.FigurateNumber(2882,'square')).square,True)
        self.assertEqual((euler61.FigurateNumber(8128,'triangle') + euler61.FigurateNumber(2882,'square')).pentagonal,False)
        self.assertEqual((euler61.FigurateNumber(8128,'triangle') + euler61.FigurateNumber(2882,'square')).hexagonal,False)
        self.assertEqual((euler61.FigurateNumber(8128,'triangle') + euler61.FigurateNumber(2882,'square')).heptagonal,False)
        self.assertEqual((euler61.FigurateNumber(8128,'triangle') + euler61.FigurateNumber(2882,'square')).octagonal,False)
        with self.assertRaises(ValueError):
            euler61.FigurateNumber(8128,'triangle') + euler61.FigurateNumber(2882,'triangle')
            euler61.FigurateNumber(8128,'triangle') + euler61.FigurateNumber(2982,'square')


    def test_appendFigurate(self):
        """Test the appendFigurate function"""
        a = euler61.FigurateNumber(8128,'triangle')
        b = euler61.FigurateNumber(2882,'square')
        c = euler61.FigurateNumber(8281,'pentagonal')
        ans = euler61.appendFigurate([a,],[b,c])[0]
        self.assertEqual(ans.n,'81282882')
        ans = euler61.appendFigurate([ans,],[b,c])[0]
        self.assertEqual(ans.n,'812828828281')

    def test_doesWrap(self):
        a = euler61.FigurateNumber(8128,'triangle')
        b = euler61.FigurateNumber(2882,'square')
        c = euler61.FigurateNumber(8281,'pentagonal')
        n = a + b + c
        self.assertEqual(euler61.doesWrap([n,])[0].n, '812828828281')

if __name__ == '__main__':
    unittest.main()