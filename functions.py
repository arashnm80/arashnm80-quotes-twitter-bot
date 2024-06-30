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

def bold_text(text):
    bold_chars = {
        'A': '𝐀', 'B': '𝐁', 'C': '𝐂', 'D': '𝐃', 'E': '𝐄', 'F': '𝐅', 'G': '𝐆', 'H': '𝐇', 'I': '𝐈', 'J': '𝐉',
        'K': '𝐊', 'L': '𝐋', 'M': '𝐌', 'N': '𝐍', 'O': '𝐎', 'P': '𝐏', 'Q': '𝐐', 'R': '𝐑', 'S': '𝐒', 'T': '𝐓',
        'U': '𝐔', 'V': '𝐕', 'W': '𝐖', 'X': '𝐗', 'Y': '𝐘', 'Z': '𝐙',
        'a': '𝐚', 'b': '𝐛', 'c': '𝐜', 'd': '𝐝', 'e': '𝐞', 'f': '𝐟', 'g': '𝐠', 'h': '𝐡', 'i': '𝐢', 'j': '𝐣',
        'k': '𝐤', 'l': '𝐥', 'm': '𝐦', 'n': '𝐧', 'o': '𝐨', 'p': '𝐩', 'q': '𝐪', 'r': '𝐫', 's': '𝐬', 't': '𝐭',
        'u': '𝐮', 'v': '𝐯', 'w': '𝐰', 'x': '𝐱', 'y': '𝐲', 'z': '𝐳',
        '0': '𝟎', '1': '𝟏', '2': '𝟐', '3': '𝟑', '4': '𝟒', '5': '𝟓', '6': '𝟔', '7': '𝟕', '8': '𝟖', '9': '𝟗',
        '.': '⦁', ',': '⠂', ';': ';', ':': '˸', '!': '！', '?': '？', '-': '‐', '(': '⁽', ')': '⁾', '&': '＆',
        '@': '＠', '#': '＃', '$': '＄', '%': '％', '^': '＾', '*': '＊', '+': '＋', '=': '＝', '_': '＿'
    }
    return ''.join(bold_chars.get(c, c) for c in text)
