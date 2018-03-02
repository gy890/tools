# coding=utf-8
"""
Created on 2017-07-10

@Filename: timeit
@Author: Gui


"""
from time import time


def timeit(func):
    def wrapped(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print('{} costs {} s.'.format(func.__name__, t2-t1))
        return result
    return wrapped
