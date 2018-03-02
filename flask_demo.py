# coding=utf-8
"""
Created on 2017-07-04

@Filename: flask_demo
@Author: Gui


"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template("index.html",
                           title="Home",
                           user=user)
