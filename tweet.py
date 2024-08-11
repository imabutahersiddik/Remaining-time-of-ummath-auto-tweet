import tweepy
import os
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

# Your Twitter App settings (replace with your actual values)
CLIENT_ID = os.environ['TWITTER_CLIENT_ID']
CLIENT_SECRET = os.environ['TWITTER_CLIENT_SECRET']

def get_bearer_token():
    """Fetches a bearer token using your app credentials."""
    client = BackendApplicationClient(client_id=CLIENT_ID)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(
        token_url='https://api.twitter.com/oauth2/token',
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
    return token['access_token']

def post_tweet(tweet_text):
    """Posts a tweet using the provided text and bearer token."""
    bearer_token = get_bearer_token()
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    data = {"text": tweet_text}
    response = requests.post(
        "https://api.twitter.com/2/tweets",
        headers=headers,
        json=data
    )
    if response.status_code != 201:
        raise Exception(f"Request returned an error: {response.status_code} {response.text}")
    print("Tweet posted successfully!")

if __name__ == "__main__":
    # ... (Your existing code to calculate remaining days)

    tweet_message = f"🚨 Another day passed! There are {remaining_years} years and {remaining_days} days remaining until the end of Ummath 2080. #Ummath #Countdown #MuslimCommunity #Faith"
    post_tweet(tweet_message)
