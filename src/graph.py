#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:52:07 2019

@author: khanhnguyen
"""

import pandas as pd
import numpy as np
import tf_dif 
import sentiment
from datetime import datetime
import matplotlib.pyplot as plt

from plotly.offline import plot
import plotly.graph_objects as go
# Offline mode
#from plotly.offline import init_notebook_mode, iplot
#init_notebook_mode(connected = True)


reviews = sentiment.get_review()
reviews = reviews.sort_values(by='Time')
date =  reviews['Time']
sentiment = reviews['Sentiment']
reviews_data = pd.DataFrame({'Time': date, 'Sentiment': sentiment})
reviews_data['Time'] = pd.to_datetime(reviews_data['Time'], format='%Y-%m-%d')
reviews_data = reviews_data.reset_index(drop=True)

def gcolor(val):
    if val < 0:
        color = 'green'
    elif val == 0:
        color = 'yellow'
    elif val > 0:
        color = 'red'
    return color

def get_colors(sentiments):
    sentiment_list = list(sentiments)
    colors = []
    for values in sentiment_list:
        color = gcolor(values)
        colors.append(color)
    return colors

col = get_colors(reviews_data.Sentiment)

new_data = go.Scatter(x=reviews_data.Time,
                         y=reviews_data.Sentiment, mode = 'markers',
                         opacity = 0.8, marker = dict(color = col))
layout = go.Layout(
                   title='JetBlue Sentiment Plot',
                   # Same x and first y
                   xaxis=dict(title='Date'),
                   yaxis=dict(title='Sentiment', color='red') 
                   )
fig = go.Figure(data=[new_data], layout=layout)


#fig.add_scattergl(x = xs, y = df.y.where(df.y <= 35), line ={‘color’ : ‘green’})
'''fig = go.Figure(go.Scatter(x=reviews_data.index,
                         y=reviews_data.Sentiment, mode = 'markers',
                         opacity = 0.8))
fig.add_scatter(x= reviews_data.index, 
                  y=  reviews_data.Sentiment.where(reviews_data.Sentiment >= 0), 
                  marker={'color': 'red'})

fig.add_scatter(x= reviews_data.index, 
                  y=reviews_data.Sentiment.where(reviews_data.Sentiment < 0), 
                  marker={'color': 'blue'}) '''
plot(fig) 








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
    