from functions import *

if __name__ == "__main__":
    quotes_list = get_quotes_list()
    tweet_text = random.choice(quotes_list)
    # tweet_text = bold_text(tweet_text)
    # tweet_text = today_date() + "\n\n" + tweet_text
    if len(tweet_text) > 280:
        print("tweet text more than 280 characters")
    else:
        print(tweet_text)
        post_tweet(tweet_text)
