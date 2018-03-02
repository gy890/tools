# coding=utf-8
"""
Created on 2017-07-03

@Filename: unittest_demo
@Author: Gui


"""
from calculator import Calculator
import unittest


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.cal = Calculator(2, 4)

    def test_add(self):
        self.assertEqual(self.cal.add(), 6)

    def test_sub(self):
        self.assertEqual(self.cal.sub(), 2)

    def test_mul(self):
        self.assertEqual(self.cal.mul(), 2)

    def test_div(self):
        self.assertEqual(self.cal.div(), 2)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CalculatorTest('test_add'))
    suite.addTest(CalculatorTest('test_sub'))
    suite.addTest(CalculatorTest('test_mul'))
    suite.addTest(CalculatorTest('test_div'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
