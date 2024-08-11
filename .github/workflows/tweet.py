import tweepy
import requests_oauthlib
import os

def get_bearer_token(consumer_key, consumer_secret):
    """Obtains a bearer token using the Client Credentials Grant flow."""
    url = "https://api.twitter.com/oauth2/token"
    data = {"grant_type": "client_credentials"}
    auth = requests_oauthlib.OAuth1Session(consumer_key, consumer_secret)
    response = auth.post(url, data=data)
    response.raise_for_status() 
    return response.json()["access_token"]

def post_tweet(tweet_text, bearer_token):
    """Posts a tweet using the provided bearer token."""
    client = tweepy.Client(bearer_token=bearer_token)
    client.create_tweet(text=tweet_text)

if __name__ == "__main__":
    consumer_key = os.environ["TWITTER_CLIENT_ID"]
    consumer_secret = os.environ["TWITTER_CLIENT_SECRET"]
    remaining_years = os.environ["remaining_years"]
    remaining_days = os.environ["remaining_days"]

    tweet_message = f"🚨 Another day passed! There are {remaining_years} years and {remaining_days} days remaining until the end of Ummath 2080. #Ummath #Countdown #MuslimCommunity #Faith"

    bearer_token = get_bearer_token(consumer_key, consumer_secret)
    post_tweet(tweet_message, bearer_token)
    print("Tweet posted successfully!")
