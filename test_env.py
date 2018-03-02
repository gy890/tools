# coding=utf-8
"""
Created on 2017-06-14

@Filename: test_env
@Author: Gui


"""


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World"]
