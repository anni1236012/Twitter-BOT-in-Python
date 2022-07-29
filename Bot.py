import os
import tweepy
from dotenv import load_dotenv
import time
load_dotenv()

API_KEY              =   os.getenv("API_KEY")
API_KEY_SECRET       =   os.getenv("API_KEY_SECRET")
ACCESS_TOKEN         =   os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET  =   os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit= True)

statusId = []

while True:
    for tweet in api.search_tweets("WEB3 OR Blockchain OR JavaScript OR Python -is:retweet -is:reply lang:en"):
        try:
            if tweet.id not in statusId:
                if tweet.text[:2] != 'RT' and not tweet.in_reply_to_screen_name and not tweet.in_reply_to_status_id:
                    print(f"Tweet Id : {tweet.id}")
                    print(f"https://twitter.com/{tweet.author.screen_name}/status/{tweet.id}")
                    api.create_favorite(tweet.id)
                    api.retweet(tweet.id)
                    statusId.append(tweet.id)
            time.sleep(7)
        except Exception as err:
            print(f"Error while retweeting \n{err}")
        
