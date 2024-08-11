const Twitter = require('twitter-lite');

// Twitter API credentials
const client = new Twitter({
  consumer_key: process.env.TWITTER_API_KEY,
  consumer_secret: process.env.TWITTER_API_SECRET_KEY,
  access_token_key: process.env.TWITTER_ACCESS_TOKEN,
  access_token_secret: process.env.TWITTER_ACCESS_TOKEN_SECRET,
});

// Function to post a tweet
const postTweet = async (tweet) => {
  try {
    await client.post("statuses/update", { status: tweet });
    console.log("Tweet posted successfully!");
  } catch (error) {
    console.error("Error posting tweet:", error);
  }
};

// Get the remaining years and days from environment variables
const remainingYears = process.env.REMAINING_YEARS;
const remainingDays = process.env.REMAINING_DAYS;

// Create the tweet message
const tweetMessage = `🚨 Another day passed! There are ${remainingYears} years and ${remainingDays} days remaining until the end of Ummath 2080. #Ummath #Countdown #MuslimCommunity #Faith`;

// Post the tweet
postTweet(tweetMessage)
