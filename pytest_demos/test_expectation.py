# coding=utf-8
"""
Created on 2017-06-19

@Filename: test_expectation
@Author: Gui


"""
import pytest


@pytest.mark.parametrize('test_input, excepted', [
    ('3+5', 8),
    ('2+4', 6),
    # ('6*9', 42),
    pytest.param('7*7', 44, marks=pytest.mark.xfail)
])
def test_eval(test_input, excepted):
    assert eval(test_input) == excepted
