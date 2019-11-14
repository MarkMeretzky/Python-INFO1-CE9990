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
    tweets = api.search("Trump", count = 3) #tweets is iterable.
except tweepy.error.TweepError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

def replaceEmojis(s):
    """
    Return the argument string with each of its emojis (i.e., any character that
    does not belong to the BMP) replaced by the Unicode replacement character.
    """
    listOfCharacters = ["\uFFFD" if ord(c) >= 0x10000 else c for c in s]
    return "".join(listOfCharacters)   #Change the list back into a string.

for tweet in tweets:
    print(f"Created at = {tweet.created_at}")
    print(f"Author = {replaceEmojis(tweet.author.name)}")
    print(f"Screen name = {tweet.author.screen_name}")
    print(f"Friends count = {tweet.author.friends_count}")
    print(f"Followers count = {tweet.author.followers_count}")
    print(f"Retweet count = {tweet.retweet_count}")
    print(f"Place = {tweet.place}")
    print(f"Source = {tweet.source}")
    print(f"Source URL = {tweet.source_url}")
    print(f"Length = {len(tweet.text)}")
    print(replaceEmojis(tweet.text))
    print(80 * "-")

sys.exit(0)
