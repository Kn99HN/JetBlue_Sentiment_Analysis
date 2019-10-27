#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:52:07 2019

@author: khanhnguyen
"""

import pandas as pd
import tf_dif 
import sentiment
from plotly.offline import plot
import plotly.graph_objects as go

#Set up the data 
reviews = sentiment.get_review()
tweets = sentiment.get_tweet()

def gcolor(val):
    if val < 0:
        color = 'red'
        sentiment = 'Negative'
    elif val == 0:
        color = 'darkblue'
        sentiment = 'Neutral'
    elif val > 0:
        color = 'green'
        sentiment = 'Positive'
    return color, sentiment

def parse_string(tweet):
    clean_tw = tweet.replace('\"','')
    clean_tw = tweet.replace('\'','')
    if 'b' in clean_tw:
        clean_tw = tweet.replace('b', '')
    if 'AT_USER' in clean_tw:
        clean_tw = clean_tw.replace('AT_USER','@user')
    if 'URL' in clean_tw:
        clean_tw = clean_tw.replace('URL','')
    return clean_tw

def get_colors(data):
    sentiment_list = list(data.Sentiment)
    colors = []
    rank_sent = []
    for values, tweet in zip(sentiment_list, data.Tweet):
        color, sent_val = gcolor(values)
        tweet = parse_string(tweet)
        sent_val += "<br>" + tweet 
        rank_sent.append(sent_val)
        colors.append(color)
    return colors, rank_sent

def plot_all_tweets(data):
    data = data.sort_values(by='Time')
    data['Time'] = pd.to_datetime(data['Time'], format='%Y-%m-%d')
    
    #Get the color 
    col, sent_list = get_colors(data)
    new_texts = join_text(sent_list)
    new_data = go.Scatter(x=data.Time,
                         y=data.Sentiment, mode = 'markers',
                         opacity = 1, 
                         marker = dict(size=12,line=dict(width=2,
                        color='DarkSlateGrey'), color = col), 
                         hovertext = new_texts, hoverinfo = "text" 
                          )
    layout = go.Layout(
                    plot_bgcolor='rgba(10,10,10)',
                   title=go.layout.Title(text="JetBlue Sentiment Analysis", 
                                         xref="paper", x=0),
                   # Same x and first y
                   xaxis= go.layout.XAxis(
                           title= go.layout.xaxis.Title(text='Date',
                                   font=dict(family='Courier New, monospace',
                                             size=20,
                                             color='darkblue'))),
                    yaxis=go.layout.YAxis(
                            title=go.layout.yaxis.Title(text='Sentiment Score', 
                                   font=dict(family='Courier New, monospace',
                                             size=20,color='darkblue'))))
    fig = go.Figure(data=[new_data], layout=layout)
    plot(fig, filename = 'templates/twitterplot.html', auto_open = False) 
    
def get_colors_review(data):
    sentiment_list = list(data.Sentiment)
    colors = []
    rank_sent = []
    for values, review in zip(sentiment_list, data.Review):
        color, sent_val = gcolor(values)
        review = parse_string(review)
        sent_val += "<br>" + review 
        rank_sent.append(sent_val)
        colors.append(color)
    return colors, rank_sent

def join_text(string_list):
    new_text = []
    for word in string_list:
        short = word.split()
        n = 5
        short = [' '.join(short[x:x+n]) for x in range(0, len(short), n)]
        text = '<br>'.join(short)
        new_text.append(text)
    return new_text
    
def plot_all_reviews(data):
    data = data.sort_values(by='Time')
    data['Time'] = pd.to_datetime(data['Time'], format='%Y-%m-%d')
    
    #Get the color 
    col, sent_list = get_colors_review(data)
    new_texts = join_text(sent_list)
    new_data = go.Scatter(x=data.Time,
                         y=data.Sentiment, mode = 'markers',
                         opacity = 1, 
                         marker = dict(size=12,line=dict(width=2,
                        color='DarkSlateGrey'), color = col), hoverinfo = "text",
                         hovertemplate = '<br><b>Sentiment Score: </b>: %{y}<br>'
                                         '<b>%{text}</b>',
                        text = new_texts
                          )
    layout = go.Layout(
                    plot_bgcolor='rgba(10,10,10)',
                   title=go.layout.Title(text="JetBlue Sentiment Analysis", 
                                         xref="paper", x=0),
                   # Same x and first y
                   xaxis= go.layout.XAxis(
                           title= go.layout.xaxis.Title(text='Date',
                                   font=dict(family='Courier New, monospace',
                                             size=20,
                                             color='darkblue'))),
                    yaxis=go.layout.YAxis(
                            title=go.layout.yaxis.Title(text='Sentiment Score', 
                                   font=dict(family='Courier New, monospace',
                                             size=20,color='darkblue'))))
    fig = go.Figure(data=[new_data], layout=layout)
    plot(fig, filename = 'templates/reviewplot.html', auto_open = False) 


plot_all_tweets(tweets)
plot_all_reviews(reviews)


    