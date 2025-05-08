import os
import tweepy
import random
from dotenv import load_dotenv
import time

load_dotenv()

# إعداد مفاتيح تويتر
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

# كلمات الرابرز
lyrics = [
    "كلمة من رابر 1",
    "كلمة من رابر 2",
    "كلمة من رابر 3",
    "كلمة من رابر 4",
]

# اختيار جملة عشوائية
tweet = random.choice(lyrics)
api.update_status(tweet)
print("تم نشر التغريدة:", tweet)
