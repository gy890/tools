# coding=utf-8
"""
Created on 2017-07-04

@Filename: class_method_demo
@Author: Gui


"""


class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


a = A()
a.foo(2)
a.class_foo(2)
a.static_foo(2)
