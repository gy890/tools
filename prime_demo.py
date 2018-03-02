# coding=utf-8
"""
Created on 2017-05-10

@Filename: prime_demo
@Author: Gui


"""


def is_prime(a, b):
    b = b + 1
    # for each in range(a, b):
    #     c = []
    #     for i in range(2, each):
    #         if each % i == 0:
    #             c.append(i)
    #     if len(c) == 0:
    #         print(each)
    prime = filter(lambda x: not [x % i for i in range(2, x) if x % i == 0], range(a, b))
    return prime

if __name__ == '__main__':
    # start = int(input('Enter a start number: '))
    # stop = int(input('Enter a stop Number: '))
    # is_prime(start, stop)
    for each in is_prime(2, 200):
        print(each)
    print(len(list(is_prime(2, 200))))

