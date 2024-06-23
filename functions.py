from variables import *

import tweepy
import requests
import random
import json
from datetime import date

def post_tweet(tweet_text):

    client = tweepy.Client(
        bearer_token=TWITTER_BEARER_TOKEN,
        consumer_key=TWITTER_CONSUMER_KEY, consumer_secret=TWITTER_CONSUMER_SECRET,
        access_token=TWITTER_ACCESS_TOKEN, access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
    )

    response = client.create_tweet(
        text = tweet_text
    )

    print(response.data)
    print(f"https://twitter.com/user/status/{response.data['id']}")

def get_quotes_list():
    api_url = quotes_page_link
    
    response = requests.get(api_url)
    if response.status_code == requests.codes.ok:
        # Split the text by newline character and filter out empty strings
        quotes_list = [line for line in response.text.split('\n') if line.strip()]

        # throw away first 5 lines which are titels
        quotes_list = quotes_list[5:]

        # throw away 2 first chars of each line which are "- "
        quotes_list = [item[2:] for item in quotes_list]

        return quotes_list
    else:
        print("Error:", response.status_code, response.text)

def today_date():
    today = date.today()
    formatted_date = today.strftime("%Y-%m-%d")
    return formatted_date
