import tweepy
import time
from keys import *

file_name = "since_id.txt"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def save_since_id(id, file_name):
    with open(file_name, 'w', encoding = 'utf-8') as file:
        file.write(str(id))

def get_since_id(file_name):
    since_id = 0
    with open(file_name, 'r', encoding = 'utf-8') as file:
        since_id = int(file.read().strip())
    return since_id


def get_mentions() :
    since_id = get_since_id(file_name)
    mentions = api.mentions_timeline(since_id = since_id, tweet_mode = 'extended')
    for mention in reversed(mentions):
        print("retrieving unseen mentioned tweets & replying")
        save_since_id(mention.id,file_name)
        print(str(mention.id)+str(mention.full_text))
        if '#postoinsta' in mention.full_text.lower():
            print('found #postoinsta')
            print('posting to instagram')
            # TODO: fnction for posting to instagrams
            api.update_status('@' + mention.user.screen_name + ' Posted successfully', mention.id)
            print('posted successfully')



while True:
    get_mentions()
    time.sleep(15)
