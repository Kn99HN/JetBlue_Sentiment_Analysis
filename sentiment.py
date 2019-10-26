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

jetblue = sentiment()

def process_rev(rev):
    if 'b' in rev: 
        if 'b\'' in rev: 
            rev = rev.split('b\'',1)
        else:
            rev = rev.split('b\"',1)
        rev = rev[1]
    return rev

def get_review():
    col_names = ['Review']
    review = pd.read_csv('review.csv', names = col_names, encoding = 'utf-8')
    reviews = review['Review']
    sentiments = []
    for rev in reviews:
        rev = process_rev(rev)
        value = get_sentiment(rev)
        sentiments.append(value)
    review['Sentiment'] = sentiments
    return review

review = get_review()
review.hist()




    
