# coding=utf-8
"""
Created on 2017-05-11

@Filename: chrome_demo
@Author: Gui


"""
import os
import unittest
from selenium import webdriver


class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        profile_dir = r"C:\Users\Gui\AppData\Local\Google\Chrome\User Data"  # 对应你的chrome的用户数据存放路径
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("user-data-dir=" + os.path.abspath(profile_dir))
        # chrome_options.add_argument("--disable-infobars")
        # chrome_options.add_argument("--start-maximized")
        # self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)
        self.browser.get('https://play.google.com/store/apps/collection/topselling_free')
        self.browser.implicitly_wait(30)
        js = "var q=document.documentElement.scrollTop=10000"
        print('dedgedgt')
        self.browser.execute_script(js)

if __name__ == '__main__':
    unittest.main(verbosity=2)
