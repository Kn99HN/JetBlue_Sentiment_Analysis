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

def get_tweet():
    col_names = ['Time','Tweet']
    jetblue = pd.read_csv(r'../Data/jetblue.csv', names = col_names)
    tweets = list(jetblue['Tweet'])
    sentiments = []
    for tweet in tweets:
        value = get_sentiment(tweet)
        sentiments.append(value)
    jetblue['Sentiment'] = sentiments
    return jetblue

def get_review():
    col_names = ['Time','Review']
    review = pd.read_csv(r'../Data/review.csv', names = col_names, 
                         encoding = 'utf-8')
    reviews = review['Review']
    sentiments = []
    for rev in reviews:
        value = get_sentiment(rev)
        sentiments.append(value)
    review['Sentiment'] = sentiments
    return review

review = get_review()




    
