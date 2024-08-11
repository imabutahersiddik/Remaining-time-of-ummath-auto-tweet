import tweepy
import os
import datetime

# Get Twitter API credentials from environment variables
consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_API_SECRET_KEY']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Calculate remaining days and years
def calculate_remaining_time():
    current_date = datetime.date.today()
    end_date = datetime.date(2080, 9, 4)
    remaining_time = (end_date - current_date).days
    remaining_years = remaining_time // 365
    remaining_days = remaining_time % 365
    return remaining_years, remaining_days

# Post the tweet
def post_tweet():
    remaining_years, remaining_days = calculate_remaining_time()
    tweet_message = f"🚨 Another day passed! There are {remaining_years} years and {remaining_days} days remaining until the end of Ummath 2080. #Ummath #Countdown #MuslimCommunity #Faith"
    api.update_status(tweet_message)
    print("Tweet posted successfully!")

if __name__ == "__main__":
    post_tweet()
