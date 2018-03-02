# coding=utf-8
"""
Created on 2017年2月28日

@author: EP-Admin
"""
import json


def main():
    with open('getRecentOrdersForEachShip.json') as f:
        data = json.load(f)
        ship_list = data.get('response').get('entries')
        print('*' * 32)
        print('{} ships'.format(len(ship_list)))
        for _i, each in enumerate(ship_list, 1):
            print(each['ship']['name'])

if __name__ == '__main__':
    main()
