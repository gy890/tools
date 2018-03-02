# coding=utf-8
"""
Created on 2017-05-11

@Filename: firefox_demo
@Author: Gui


"""
from selenium import webdriver
import time
import os

fp = webdriver.FirefoxProfile(r'C:\Users\Gui\AppData\Roaming\Mozilla\Firefox\Profiles\pg1j7ph2.default')
browser = webdriver.Firefox(fp)
browser.maximize_window()
browser.get("http://www.baidu.com")