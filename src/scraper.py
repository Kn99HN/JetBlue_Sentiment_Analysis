#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:44:30 2019

@author: khanhnguyen
"""

import bs4
import requests
import csv 
def parse_review(text):
    if '|' in text: 
        text = text.split('|')
        return text[1]
    else:
        return text

def get_soup(res):
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    return soup.find_all('div', {"class": "body"})


def write_csv():
    csvFile = open(r'../Data/review.csv', 'a')
    # Makes sures line ends with one new line
    csvWriter = csv.writer(csvFile)
    return csvWriter

def get_reviews():
    csvWriter = write_csv()
    for page in range(1,75):
        url = 'https://www.airlinequality.com/airline-reviews/jetblue-airways'
        url += '/page/' + str(page) + '/'
        res = requests.get(url)
        soup = get_soup(res)
        for review in soup:
            rev = review.find('div',{"class": "text_content"}).text
            rev = str(parse_review(rev))
            date = review.find('time').attrs['datetime'] 
            review = str(parse_review(rev))
            if "Read more" in review:
                continue
            csvWriter.writerow([date, review])
    

            
#review = get_reviews()

