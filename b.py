# coding=utf-8
"""
Created on 2017-06-27

@Filename: b
@Author: Gui


"""
import unittest
import time


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("start!")

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        print("end!")

    def test01(self):
        print("执行测试用例01")
        self.assertTrue(None)

    def test03(self):
        print("执行测试用例03")

    def test02(self):
        print("执行测试用例02")

    def addtest(self):
        print("add方法")


if __name__ == "__main__":
    # unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(Test('test02'))
    # suite.addTest(Test('test01'))
    # suite.addTest(Test('test03'))
    # print(suite.countTestCases())
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
