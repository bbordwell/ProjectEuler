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
        """Tests for writtennumber"""
        self.assertEqual(usefulfunctions.writtennumber(193),'onehundredninetythree')
        self.assertEqual(usefulfunctions.writtennumber(75,withand=True),'seventyfive')
        self.assertEqual(usefulfunctions.writtennumber(233,withspaces=True),'two hundred thirtythree')
        self.assertEqual(usefulfunctions.writtennumber(818,withhyphen=True),'eighthundredeighteen')
        self.assertEqual(usefulfunctions.writtennumber(438,withand=True,withspaces=True),'four hundred and thirtyeight')
        self.assertEqual(usefulfunctions.writtennumber(279,withand=True,withhyphen=True),'twohundredandseventy-nine')
        self.assertEqual(usefulfunctions.writtennumber(635,withspaces=True,withhyphen=True),'six hundred thirty-five')
        self.assertEqual(usefulfunctions.writtennumber(974,withand=True,withspaces=True,withhyphen=True),'nine hundred and seventy-four')

    def test_sieveOfEratosthenes(self):
        """Tests for sieveOfEratosthenes"""
        self.assertEqual(usefulfunctions.sieve_of_Eratosthenes(41),[2,3,5,7,11,13,17,19,23,29,31,37])

    def test_pythagoreanTriples(self):
        """Tests for pythagoreanTriples."""
        self.assertEqual(usefulfunctions.pythagoreanTriples(100),[(3,4,5),(5,12,13),
        (6,8,10),(7,24,25),(8,15,17),(9,12,15),(9,40,41),(10,24,26),(11,60,61),
        (12,16,20),(12,35,37),(13,84,85),(14,48,50),(15,20,25),(15,36,39),
        (16,30,34),(16,63,65),(18,24,30),(18,80,82),(20,21,29),(20,48,52),
        (21,28,35),(21,72,75),(24,32,40),(24,45,51),(24,70,74),(25,60,65),
        (27,36,45),(28,45,53),(28,96,100),(30,40,50),(30,72,78),(32,60,68),
        (33,44,55),(33,56,65),(35,84,91),(36,48,60),(36,77,85),(39,52,65),
        (39,80,89),(40,42,58),(40,75,85),(42,56,70),(45,60,75),(48,55,73),
        (48,64,80),(51,68,85),(54,72,90),(57,76,95),(60,63,87),(60,80,100),
        (65,72,97)])

    def test_triangleNumbersGenerator(self):
        """Tests for triangleNumbersGenerator"""
        self.assertEqual(list(usefulfunctions.triangleNumbersGenerator(10)),[1,3,6,10,15,21,28,36,45,55])
        triangleNumbers = usefulfunctions.triangleNumbersGenerator()
        nums = []
        for trianglenumber in range(10):
            nums.append(triangleNumbers.__next__())
        self.assertEqual(nums,[1,3,6,10,15,21,28,36,45,55])

    def test_phis(self):
        """Tests for phis."""
        correctPhis = {2: 1, 3: 2, 4: 2, 5: 4, 6: 2, 7: 6, 8: 4, 9: 6, 10: 4, 11: 10,
                      12: 4, 13: 12, 14: 6, 15: 8, 16: 8, 17: 16, 18: 6, 19: 18, 20: 8,
                      21: 12, 22: 10, 23: 22, 24: 8, 25: 20, 26: 12, 27: 18, 28: 12,
                      29: 28, 30: 8, 31: 30, 32: 16, 33: 20, 34: 16, 35: 24, 36: 12,
                      37: 36, 38: 18, 39: 24, 40: 16, 41: 40, 42: 12, 43: 42, 44: 20,
                      45: 24, 46: 22, 47: 46, 48: 16, 49: 42, 50: 20, 51: 32, 52: 24,
                      53: 52, 54: 18, 55: 40, 56: 24, 57: 36, 58: 28, 59: 58, 60: 16,
                      61: 60, 62: 30, 63: 36, 64: 32, 65: 48, 66: 20, 67: 66, 68: 32,
                      69: 44, 70: 24, 71: 70, 72: 24, 73: 72, 74: 36, 75: 40, 76: 36,
                      77: 60, 78: 24, 79: 78, 80: 32, 81: 54, 82: 40, 83: 82, 84: 24,
                      85: 64, 86: 42, 87: 56, 88: 40, 89: 88, 90: 24, 91: 72, 92: 44, 
                      93: 60, 94: 46, 95: 72, 96: 32, 97: 96, 98: 42, 99: 60, 100: 40}
        self.assertEqual(usefulfunctions.phis(100),correctPhis)

    def test_primeFactorsOfRange(self):
        """Tests for primeFactorsOfRange."""
        correctFactors = {2: (), 3: (), 4: (2,), 5: (), 6: (2, 3), 7: (), 8: (2,), 
                          9: (3,), 10: (2, 5), 11: (), 12: (2, 3), 13: (), 14: (2, 7), 
                          15: (3, 5), 16: (2,), 17: (), 18: (2, 3), 19: (), 20: (2, 5), 
                          21: (3, 7), 22: (2, 11), 23: (), 24: (2, 3), 25: (5,), 
                          26: (2, 13), 27: (3,), 28: (2, 7), 29: (), 30: (2, 3, 5)}
        self.assertEqual(correctFactors,usefulfunctions.primeFactorsOfRange(30))





if __name__ == '__main__':
    unittest.main()