"""
tweepy.py

Print the most recent tweets that mention Mayor DeBlasio.
"""

import sys
import tweepy

#To get these four strings, go to https://apps.twitter.com/app/new
#Create a Twitter application, then click on Keys and Access Tokens tab.

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

authenticationHandler = tweepy.OAuthHandler(consumer_key, consumer_secret)
authenticationHandler.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth_handler = authenticationHandler)

try:
    tweets = api.search("DeBlasio", count = 3)
except tweepy.error.TweepError as tweepError:
    print(tweepError)
    sys.exit(1)

def replaceEmojis(s):
    for i, c in enumerate(s):
        if ord(c) >= 0x10000:                #if c does not belong to the BMP,
            s = c[:i] + "\uFFFD" + s[i+1:]   #change c to the replacement char.
    return s

for tweet in tweets:
    print("Created at =", tweet.created_at)
    print("Author =", replaceEmojis(tweet.author.name))
    print("Screen name =", tweet.author.screen_name)
    print("Friends count =", tweet.author.friends_count)
    print("Followers count =", tweet.author.followers_count)
    print("Retweet count =", tweet.retweet_count)
    print("Source =", tweet.source)
    print("Length =", len(tweet.text))
    print(replaceEmojis(tweet.text))
    print(80 * "-")

sys.exit(0)
