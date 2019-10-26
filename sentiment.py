#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:44:22 2019

@author: khanhnguyen
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
def get_sentiment(media):
    score = analyzer.polarity_scores(media)
    return score['compound']
