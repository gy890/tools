# coding=utf-8
"""
Created on 2017-06-19

@Filename: test_params
@Author: Gui


"""
import pytest


@pytest.fixture(params=[1, 2, 3])
def test_data(request):
    return request.param


def test_not_2(test_data):
    print('test_data: %s' % test_data)
    assert test_data !=2
