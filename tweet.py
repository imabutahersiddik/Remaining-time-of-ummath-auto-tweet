import tweepy
import os

def post_tweet(api_key, api_secret, access_token, access_token_secret, message):
    """Posts a tweet using the provided Twitter API credentials.

    Args:
        api_key (str): Your Twitter API key.
        api_secret (str): Your Twitter API secret key.
        access_token (str): Your Twitter access token.
        access_token_secret (str): Your Twitter access token secret.
        message (str): The tweet message to post.
    """

    # Authenticate with the Twitter API
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        # Post the tweet
        api.update_status(message)
        print("Tweet posted successfully!")
    except tweepy.TweepError as error:
        print(f"Error posting tweet: {error}")


if __name__ == "__main__":
    # Get Twitter API credentials from environment variables
    api_key = os.environ['TWITTER_API_KEY']
    api_secret = os.environ['TWITTER_API_SECRET_KEY']
    access_token = os.environ['TWITTER_ACCESS_TOKEN']
    access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

    # Example tweet message
    tweet_message = "This is a test tweet from Tweepy!"

    # Post the tweet
    post_tweet(api_key, api_secret, access_token, access_token_secret, tweet_message)
