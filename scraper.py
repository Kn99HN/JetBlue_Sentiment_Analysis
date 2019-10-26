#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:44:30 2019

@author: khanhnguyen
"""

import bs4
import requests

res = requests.get('https://www.airlinequality.com/airline-reviews/jetblue-airways')
soup = bs4.BeautifulSoup(res.text)
