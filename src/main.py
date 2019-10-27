#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:48:02 2019

@author: khanhnguyen
"""
import sentiment
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
import random 
import json

twitter = sentiment.get_tweet()
aqreview = sentiment.get_review()
def gsent(val):
    if val < 0:
        sentiment = 'Negative'
    elif val == 0:
        sentiment = 'Neutral'
    elif val > 0:
        sentiment = 'Positive'
    return sentiment

def get_randint():
    return random.randint(0,734)

def randomize():
    rand_int = get_randint()
    if rand_int < 131: 
        origin = "Twitter"
        df = twitter.iloc[[rand_int]]
    else:
        origin = "Airline Quality"
        df = aqreview.iloc[[rand_int]]
    text = df['Review'].iat[0]
    score = float(df['Sentiment'])
    sentiment = gsent(score)
    return text, origin, sentiment, score

def create_json():
    text, origin, sentiment, score = randomize()
    data = {}
    data['text'] = text
    data['orgin'] = origin
    data['sentiment'] = sentiment
    data['score'] = score
    json_data = json.dumps(data)
    return json_data


@app.route('/')
def result():
    return render_template("index.html")


@app.route('/twitter_data')
def twitter_data():
    return render_template("twitter_data.html")

@app.route('/airquality_data')
def airlinequality_data():
    return render_template("airquality_data.html")


@app.route('/randomizer')
def randomizer():
    return render_template("randomizer.html")

@app.route('/receiver', methods = ['POST'])
def get_json():
    text = create_json()
    print(text)
    return text

@app.route('/about')
def about():
    return render_template("about.html")


# @app.route('/hello')
# def hello():
#     return 'Hello, World'
    

if __name__ == '__main__':
    app.run()