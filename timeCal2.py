# coding=utf-8
"""
Created on 2017-04-21

@Filename: timeCal2
@Author: Gui


"""
import time


def str_convert_timestamp():
    dt = "2016-05-05 20:28:54"
    # 转换成时间数组
    time_array = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(time_array)
    print(type(time_array), type(timestamp))
    return time_array, timestamp


def str_convert_str():
    dt = "2016-05-05 20:28:54"
    # 转换成时间数组
    time_array = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    # 转换成新的时间格式(20160505-20:28:54)
    dt_new = time.strftime("%Y%m%d-%H:%M:%S", time_array)
    print(type(time_array), type(dt_new))
    return time_array, dt_new


def timestamp_convert_str():
    timestamp = 1462451334
    # 转换成localtime
    time_local = time.localtime(timestamp)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    print(type(time_local), type(dt))
    return time_local, dt


def get_time():
    # 获取当前时间
    time_now = int(time.time())
    # 转换成localtime
    time_local = time.localtime(time_now)
    # 转换成新的时间格式(2016-05-09 18:59:20)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    print(type(time_local), type(dt))
    return time_local, dt


if __name__ == '__main__':
    print('*'*64)
    print('{}: {}'.format('str_convert_timestamp', str_convert_timestamp()))
    print('*'*64)
    print('{}: {}'.format('str_convert_str', str_convert_str()))
    print('*'*64)
    print('{}: {}'.format('timestamp_convert_str', timestamp_convert_str()))
    print('*'*64)
    print('{}: {}'.format('get_time', get_time()))
