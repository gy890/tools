# coding=utf-8
"""
Created on 2017-06-19

@Filename: test_smtpsimple
@Author: Gui


"""
import pytest


@pytest.fixture
def smtp():
    import smtplib
    return smtplib.SMTP('smtp.gmail.com')


def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    print(response)
    print(msg)
    assert response == 250
    assert 0
