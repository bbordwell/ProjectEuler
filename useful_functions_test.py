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

    def test_romanToInteger(self):
        """Tests for romanToInteger"""
        self.assertEqual(usefulfunctions.romanToInteger('III'),3)
        self.assertEqual(usefulfunctions.romanToInteger('IV'),4)
        self.assertEqual(usefulfunctions.romanToInteger('XI'),11)
        self.assertEqual(usefulfunctions.romanToInteger('XIV'),14)
        self.assertEqual(usefulfunctions.romanToInteger('XLIX'),49)
        self.assertEqual(usefulfunctions.romanToInteger('LVI'),56)
        self.assertEqual(usefulfunctions.romanToInteger('CLI'),151)
        self.assertEqual(usefulfunctions.romanToInteger('XCIX'),99)
        self.assertEqual(usefulfunctions.romanToInteger('CDXCIX'),499)
        self.assertEqual(usefulfunctions.romanToInteger('DLVI'),556)
        self.assertEqual(usefulfunctions.romanToInteger('CMXCIX'),999)
        self.assertEqual(usefulfunctions.romanToInteger('MDLXI'),1561)

    def test_ordinalNumber(self):
        """Tests for ordinalNumber"""
        self.assertEqual(usefulfunctions.ordinal_number(1),'first')
        self.assertEqual(usefulfunctions.ordinal_number(30),'thirtieth')
        self.assertEqual(usefulfunctions.ordinal_number(25),'twentyfifth')
        self.assertEqual(usefulfunctions.ordinal_number(90),'ninetieth')

    def test_farey(self):
        """Tests for farey"""
        self.assertEqual(usefulfunctions.farey(6),['0/1','1/6','1/5','1/4','1/3','2/5','1/2','3/5','2/3','3/4','4/5','5/6','1/1'])

    def test_phi(self):
        """Tests for phi"""
        self.assertEqual(usefulfunctions.phi(9),6)

    def test_arecoprime(self):
        """Tests for arecoprime"""
        self.assertEqual(usefulfunctions.arecoprime(14,25),True)
        self.assertEqual(usefulfunctions.arecoprime(14,21),False)

    def test_isprime(self):
        """tests for isprime"""
        self.assertEqual(usefulfunctions.isprime(2),True)
        self.assertEqual(usefulfunctions.isprime(2137),True)
        self.assertEqual(usefulfunctions.isprime(1865),False)

    def test_factors_of_N(self):
        """tests for factors_of_N"""
        self.assertEqual(usefulfunctions.factors_of_N(48),[1,2,3,4,6,8,12,16,24,48])
        self.assertEqual(usefulfunctions.factors_of_N(2),[1,2])
        self.assertEqual(usefulfunctions.factors_of_N(52,include_One=False),[2,4,13,26,52])
        self.assertEqual(usefulfunctions.factors_of_N(52,include_N=False),[1,2,4,13,26])
        self.assertEqual(usefulfunctions.factors_of_N(52,include_One=False,include_N=False),[2,4,13,26])

    def test_writtenumber(self):
        self.assertEqual(usefulfunctions.writtennumber(193),'onehundredninetythree')
        self.assertEqual(usefulfunctions.writtennumber(75,withand=True),'seventyfive')
        self.assertEqual(usefulfunctions.writtennumber(233,withspaces=True),'two hundred thirtythree')
        self.assertEqual(usefulfunctions.writtennumber(818,withhyphen=True),'eighthundredeighteen')
        self.assertEqual(usefulfunctions.writtennumber(438,withand=True,withspaces=True),'four hundred and thirtyeight')
        self.assertEqual(usefulfunctions.writtennumber(279,withand=True,withhyphen=True),'twohundredandseventy-nine')
        self.assertEqual(usefulfunctions.writtennumber(635,withspaces=True,withhyphen=True),'six hundred thirty-five')
        self.assertEqual(usefulfunctions.writtennumber(974,withand=True,withspaces=True,withhyphen=True),'nine hundred and seventy-four')

    def test_sieveOfEratosthenes(self):
        self.assertEqual(usefulfunctions.sieve_of_Eratosthenes(41),[2,3,5,7,11,13,17,19,23,29,31,37])

if __name__ == '__main__':
    unittest.main()