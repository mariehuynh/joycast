import tweepy

# You must create your own keys.py with a keys dict in it. Do not commit it!
from keys import keys

__all__ = ["uploadPhoto"]

SCREEN_NAME = keys['screen_name']
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def uploadPhoto(imagePath):
    api.update_with_media(imagePath, status="#MakesMeHappy #joycast")
