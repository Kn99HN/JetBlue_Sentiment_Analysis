#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:48:02 2019

@author: khanhnguyen
"""
from nltk.tokenize import word_tokenize, sent_tokenize
import math
import numpy as np 
import pandas as pd
from nltk.corpus import stopwords
import re

cachedStopWords = set(stopwords.words("english"))
def preprocess(text):
    text = ' '.join([word for word in text.split() if word not in cachedStopWords])
    #text = re.sub('[^A-z0-9 -]', '', text)
    return text

#count the word in the review
def count_words(review):
    count = 0
    words = word_tokenize(review)
    for word in words:
        count += 1
    return count

def get_doc(review):
    doc_info = []
    i = 0
    for rev in review:
        i += 1
        count = count_words(rev)
        temp = {'doc_id:' : i, 'doc_length': count}
        doc_info.append(temp)
    return doc_info

#count the frequency
def create_freq_dict(reviews):
    i = 0
    freqDict_list = []
    for review in reviews:
        i += 1
        freq_Dict = {}
        words = word_tokenize(review)
        for word in words: 
            word = word.lower()
            if word in freq_Dict:
                freq_Dict[word] += 1
            else:
                freq_Dict[word] = 1
            temp = {'id': i, 'freq_dict' : freq_Dict}
        freqDict_list.append(temp)
    return freqDict_list

def computeTF(doc_info, freqDict_list):
    '''
    tf = frequency of terms in doc / total numbers of terms in doc
    '''
    TF_scores = []
    for tempDict in freqDict_list:
        id = tempDict['id']
        for k in tempDict['freq_dict']:
            temp = {'rev_id':id, 
                    'TF_score': tempDict['freq_dict'][k] / doc_info[id - 1]['doc_length'],
                    'key': k}
            TF_scores.append(temp)
    return TF_scores

def computeIDF(doc_info, freqDict_list):
    IDF_scores = []
    counter = 0
    for dict in freqDict_list:
        counter += 1
        for k in dict['freq_dict'].keys():
            count = sum([k in tempDict['freq_dict'] for tempDict in freqDict_list])
            temp = {'rev_id': counter, 
                    'IDF_score': math.log(len(doc_info) / count), 'key': k}
            IDF_scores.append(temp)
    return IDF_scores

def computeTFIDF(TF_scores, IDF_scores):
    TFIDF_scores = []
    for j in IDF_scores:
        for i in TF_scores:
            if j['key'] == i['key'] and j['rev_id'] == i['rev_id']:
                temp = { 
                        'TFDIF_score': j['IDF_score'] * i['TF_score'],
                        'word': i['key']}
        TFIDF_scores.append(temp)
    return TFIDF_scores

def get_df(text):
    text = preprocess(text)
    text = sent_tokenize(text)
    freqDict_list = create_freq_dict(text)
    text = get_doc(text)
    TF_score = computeTF(text, freqDict_list)
    IDF_score = computeIDF(text, freqDict_list)
    TFDIF_score = computeTFIDF(TF_score, IDF_score)
    scores = []
    words = []
    for TFDIF in TFDIF_score:
        scores.append(TFDIF['TFDIF_scores'])
        words.append(TFDIF['word'])
    df = pd.DataFrame({"words":words, "scores":scores})
    df = df[df['scores'] > 0.05]
    return df

def get_max(text):
    df = get_df(text)
    max_freq = df['scores'].max()
    df = df[df['scores']] == max_freq
    return df



                
                