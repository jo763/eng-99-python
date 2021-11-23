from simple_calc import SimpleCalc
import unittest

class SimpleCalcTests(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalc()
    def test_add(self):
        actual = self.calc.add(3,4)
        expected = 7
        self.assertEqual(expected, actual)
    def test_subtract(self):
        calc = SimpleCalc()
        actual = calc.subtract(4,3)
        expected = 1
        self.assertEqual(expected, actual)
    def test_multiply(self):
        calc = SimpleCalc()
        actual = calc.multiply(4,3)
        expected = 12
        self.assertEqual(expected, actual)
    def test_divide(self):
        calc = SimpleCalc()
        actual = calc.divide(88,4)
        expected = 22
        self.assertEqual(expected, actual)
