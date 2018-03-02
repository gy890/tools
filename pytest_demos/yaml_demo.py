# coding=utf-8
"""
Created on 2017-06-19

@Filename: yaml_demo
@Author: Gui


"""
import yaml


if __name__ == '__main__':
    with open(r'D:\e-ports\ci-helper\deploy\eports\development.yml') as f:
        content = f.read()
    print(type(content), content)
    json = yaml.load(content)
    print(type(json), json)
