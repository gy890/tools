# coding=utf-8
"""
Created on 2017-05-10

@Filename: factorial_demo
@Author: Gui


"""
import functools


def add_factorial(n):
    empty_list = []
    for i in map(lambda x: x+1, range(n)):
        a = functools.reduce(lambda x, y: x*y, map(lambda x: x+1, range(i)))
        empty_list.append(a)
    return empty_list


def main():
    try:
        n = input('Enter a number(int): ')
        result = add_factorial(int(n))
        print(functools.reduce(lambda x, y: x+y, result))
    except (NameError, TypeError) as e:
        print(e)

if __name__ == '__main__':
    main()


