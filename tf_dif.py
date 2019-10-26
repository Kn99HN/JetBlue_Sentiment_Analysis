#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:48:02 2019

@author: khanhnguyen
"""
from nltk.tokenize import word_tokenize, sent_tokenize

#count the word in the review
def count_words(review):
    count = 0
    words = word_tokenize(review)
    for word in words:
        count += 1
    return count

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
            temp = {'id': i, 'freq_dict:' : freq_Dict}
        freqDict_list.append(temp)
    return freqDict_list

def computeDF(doc_info, freqDict_list):
    '''
    tf = frequency of terms in doc / total numbers of terms in doc
    '''
    TF_scores = []