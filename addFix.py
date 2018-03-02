# coding=utf-8
"""
Created on 2016年12月12日

@author: EP-Admin
"""
import os
import cchardet as chardet

if __name__ == '__main__':
    path = input('Enter the path: ').decode('utf-8')
    for each in os.listdir(path):
        result = chardet.detect(os.path.join(path, each))
        print(result)
