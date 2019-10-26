#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:48:02 2019

@author: khanhnguyen
"""

from flask import Flask, jsonify

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def root():
    return "root"

if __name__ == '__main__':
    app.run()