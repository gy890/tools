# coding=utf-8
"""
Created on 2017-04-21

@Filename: timeCal
@Author: Gui


"""
import time


def main():
    timestamp1 = 1492738644
    timestamp2 = 1492767444
    # 转换成localtime
    time_local1 = time.localtime(timestamp1)
    time_local2 = time.localtime(timestamp2)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    dt1 = time.strftime("%Y-%m-%d %H:%M:%S", time_local1)
    dt2 = time.strftime("%Y-%m-%d %H:%M:%S", time_local2)
    print(dt1, dt2)

if __name__ == '__main__':
    main()
