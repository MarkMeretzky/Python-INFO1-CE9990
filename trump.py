"""
trump.py

Print the most recent tweets that mention Trump.
"""

import sys
import tweepy   #Do not name this Python script tweepy.py.

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
    tweets = api.search("Trump", count = 3) #tweets is (like) a list.
except tweepy.error.TweepError as error:
    print(error)
    sys.exit(1)

def replaceEmojis(s):
    """
    Return the argument string with each of its emojis replaced by the
    Unicode replacement character.
    """
    s = list(s)                 #Change the string into a list of characters.
    for i, c in enumerate(s):
        if ord(c) >= 0x10000:   #if c does not belong to the BMP,
            s[i] = "\uFFFD"     #change c into the replacement character.
    return "".join(s)           #Change the list back into a string.

for tweet in tweets:
    print("Created at =", tweet.created_at)
    print("Author =", replaceEmojis(tweet.author.name))
    print("Screen name =", tweet.author.screen_name)
    print("Friends count =", tweet.author.friends_count)
    print("Followers count =", tweet.author.followers_count)
    print("Retweet count =", tweet.retweet_count)
    print("Place =", tweet.place)
    print("Source =", tweet.source)
    print("Source URL =", tweet.source_url)
    print("Length =", len(tweet.text))
    print(replaceEmojis(tweet.text))
    print(80 * "-")

sys.exit(0)
