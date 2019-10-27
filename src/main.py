#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:48:02 2019

@author: khanhnguyen
"""
import sentiment
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/')
def result():
    return render_template("index.html")


@app.route('/data')
def data():
    return render_template("data.html")


@app.route('/randomizer/', methods=['POST'])
def randomizer():
    quote = getQuote()
    return render_template("randomizer.html", quote=quote)


@app.route('/about')
def about():
    return render_template("about.html")


# @app.route('/hello')
# def hello():
#     return 'Hello, World'
    

if __name__ == '__main__':
    app.run()