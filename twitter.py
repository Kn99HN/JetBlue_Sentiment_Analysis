import tweepy as twp
import json
import csv 
import pandas as pd

keys = {}
with open("key.json","r") as f:
        keys = json.loads(f.read())
#Consumer keys and access tokens, used for OAuth
consumer_key = keys["consumer_key"]
consumer_secret = keys["consumer_secret"]
access_token = keys["access_token"]
access_secret = keys["access_secret"]

# OAuth process, using the keys and tokens
auth = twp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#Creation of the interface
tw_api = twp.API(auth)


def clean():
    colnames = ['Time', 'Tweet']
    jetblue = pd.read_csv(r'jetblue.csv', names = colnames)
    return jetblue
    
