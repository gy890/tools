import gevent
import requests


def func(url):
    print("get: %s"%url)
    gevent.sleep(0)
    date =requests.get(url)
    ret = date.text
    print(url,len(ret))

gevent.joinall([
    gevent.spawn(func, 'https://www.python.org/'),
    gevent.spawn(func, 'https://www.yahoo.com/'),
    gevent.spawn(func, 'https://github.com/'),
])