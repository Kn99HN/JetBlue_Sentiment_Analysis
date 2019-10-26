#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:44:22 2019

@author: khanhnguyen
"""
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
def get_sentiment(media):
    score = analyzer.polarity_scores(media)
    return score['compound']

def get_data():
    col_names = ['Time','Tweet']
    jetblue = pd.read_csv('jetblue.csv', names = col_names)
    return jetblue

def sentiment():
    jetblue = get_data()
    tweets = list(jetblue['Tweet'])
    sentiments = []
    for tweet in tweets:
        value = get_sentiment(tweet)
        sentiments.append(value)
    jetblue['Sentiment'] = sentiments
    return jetblue




    
