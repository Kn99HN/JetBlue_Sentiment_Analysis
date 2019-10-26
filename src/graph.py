#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:52:07 2019

@author: khanhnguyen
"""

import pandas as pd
import numpy as np
import tf_dif 
import tf_dif
import sentiment
from datetime import datetime
import matplotlib.pyplot as plt


reviews = sentiment.get_review()
dates = reviews['Time']
sentiments = reviews['Sentiment']

#date_objects = [datetime.strptime(date, '%Y-%m-%d').date() for date in dates]
#plt.scatter(date_objects, sentiments, marker = 'o')

def plot_neg():
    neg_sentiments = reviews[reviews['Sentiment'] <= -0.5]
    dates = neg_sentiments['Time']
    neg_sentiments = neg_sentiments['Sentiment']
    date_objects = [datetime.strptime(date, '%Y-%m-%d').date() for date in dates]
    plt.scatter(date_objects, neg_sentiments, marker = 'o')

def plot_positive():
    pos_sentiments = reviews[reviews['Sentiment'] >= 0.25]
    dates = pos_sentiments['Time']
    pos_sentiments = pos_sentiments['Sentiment']
    date_objects = [datetime.strptime(date, '%Y-%m-%d').date() for date in dates]
    plt.scatter(date_objects, pos_sentiments, marker = 'o')
    
#plot_neg()
plot_positive()