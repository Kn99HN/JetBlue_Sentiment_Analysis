import re

import tweepy as twp
import json
import csv

keys = {}
with open("key.json","r") as f:
        keys = json.loads(f.read())
# Consumer keys and access tokens, used for OAuth
consumer_key = keys["consumer_key"]
consumer_secret = keys["consumer_secret"]
access_token = keys["access_token"]
access_secret = keys["access_secret"]

# OAuth process, using the keys and tokens
auth = twp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


# Creation of the interface
tw_api = twp.API(auth)
def writeCSV():
    csvFile = open('jetblue.csv', 'w', newline='')
    # Makes sures line ends with one new line
    csvWriter = csv.writer(csvFile, lineterminator = '\n')
    index = 0;

    for tweet in twp.Cursor(tw_api.search,q="jetblue", tweet_mode='extended', count=100, lang="en", since="2017-04-03").items(40000):

        index +=1

        text = tweet.full_text
        # Convert to lower case
        text = text.lower()
        # Convert www.* or https?://* to URL
        text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', text)
        # Convert @username to AT_USER
        text = re.sub('@[^\s]+', 'AT_USER', text)
        # Remove additional white spaces
        text = re.sub('[\s]+', ' ', text)
        # Replace #word with word
        text = re.sub(r'#([^\s]+)', r'\1', text)
        print(index, text)
        if(filterCSV(text)):
            csvWriter.writerow([tweet.created_at, text.encode('utf-8')])
    print(tw_api)



def filterCSV(string):
    with open('jetblue.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            # print(row)
            # print(row[0])
            # print(row[1][1:])
            if compare(row[1][1:], string) == 0:
                return 0
    return 1


def compare(string1, string2):
    diff = 0;
    index = 0;
    minlen = min(len(string1), len(string2))

    for index in range(0, minlen):
        if(string1[index] == string2[index]):
            diff += 1;
    if diff/minlen <= .015:
        return 0
    return 1


writeCSV()