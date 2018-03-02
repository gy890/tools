# coding=utf-8
"""
Created on 2017年2月23日

@author: EP-Admin
"""


def parse1line(line):
    if '"' not in line:
        return None
    else:
        data = line.split('"')[3]
        return data


def parse2line(line):
    if '"' not in line:
        return None
    else:
        data = line.split('"')[1]
        return data


def main():
    with open('schemas.js', 'r') as f:
        lines = f.readlines()
    print('*' * 32)
    service = ': '.join([parse1line(lines[1]), parse1line(lines[2])])
    print(service)
    for _n, line in enumerate(lines[4:(len(lines) - 2)], 1):
        api = parse2line(line)
        print(api)
    print('*' * 32)
        
if __name__ == '__main__':
    main()
