# coding=utf-8
"""
Created on 2017-06-19

@Filename: test_class
@Author: Gui


"""


class TestClass(object):
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, 'check')
