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

csvFile = open('jetblue.csv', 'a')
# Makes sures line ends with one new line
csvWriter = csv.writer(csvFile, lineterminator = '\n')
index = 0;

for tweet in twp.Cursor(tw_api.search,q="#JetBlue", tweet_mode='extended', count=100, lang="en", since="2017-04-03").items(400):
    print(index, tweet.full_text)
    index +=1
    csvWriter.writerow([tweet.created_at, tweet.full_text.encode('utf-8')])
print(tw_api)

