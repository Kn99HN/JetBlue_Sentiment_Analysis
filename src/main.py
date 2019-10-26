#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:48:02 2019

@author: khanhnguyen
"""

from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/')
def result():
    return render_template("index.html")


# @app.route('/hello')
# def hello():
#     return 'Hello, World'

if __name__ == '__main__':
    app.run()