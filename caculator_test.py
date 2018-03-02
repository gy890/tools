# coding=utf-8
"""
Created on 2017-05-17

@Filename: caculator_test
@Author: Gui


"""
import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.cal = Calculator(8, 4)

    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual(self.cal.add(), 12)

    def test_sub(self):
        self.assertEqual(self.cal.sub(), 4)

    def test_mul(self):
        self.assertEqual(self.cal.mul(), 32)

    def test_div(self):
        self.assertEqual(self.cal.div(), 2)


if __name__ == '__main__':
    # unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(CalculatorTest('test_add'))
    # suite.addTest(CalculatorTest('test_sub'))
    # suite.addTest(CalculatorTest('test_mul'))
    # suite.addTest(CalculatorTest('test_div'))
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    suite1 = unittest.TestLoader().loadTestsFromTestCase(CalculatorTest)
    suite2 = unittest.TestSuite([suite1, ])
    unittest.TextTestRunner().run(suite2)
