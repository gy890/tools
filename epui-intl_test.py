# coding=utf-8
"""
Created on 2017-07-04

@Filename: epui-intl_test
@Author: Gui


"""
import os
path = r'D:\e-ports\ep-portal\node_modules\epui-intl\dist'
dirs = os.listdir(path)

for each in dirs:
    p = os.path.join(path, each)
    files = os.listdir(p)
    if len(files) < 2:
        print(p)
