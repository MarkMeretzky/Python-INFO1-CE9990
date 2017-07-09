"""
tweepy.py

Print the most recent texts that mention Mayor DeBlasio.
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

#The characters in the Unicode BMP (Basic Multilingual Plane) range from
#0000 to FFFF.  tkinter cannot handle larger characters, such as emojis.
#Replace all larger characters with the Unicode replacement character FFFD.
emojis = dict.fromkeys(range(0x10000, sys.maxunicode + 1), "\uFFFD")

for tweet in tweets:
    print("Created at =", tweet.created_at)
    print("Author =", tweet.author.name.translate(emojis))
    print("Screen name =", tweet.author.screen_name)
    print("Friends count =", tweet.author.friends_count)
    print("Followers count =", tweet.author.followers_count)
    print("Retweet count =", tweet.retweet_count)
    print("Source =", tweet.source)
    print("Length =", len(tweet.text))
    print(tweet.text.translate(emojis))
    print(80 * "-")

sys.exit(0)
