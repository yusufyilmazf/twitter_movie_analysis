import tweepy

consumer_key = "Your API/Consumer key" 
consumer_secret = "Your API/Consumer Secret Key" 
access_token = "Your Access token key"    
access_token_secret = "Your Access token Secret key" 

auth = tweepy.OAuth1UserHandler(
  consumer_key, 
  consumer_secret, 
  access_token, 
  access_token_secret
)

# authorize twitter
api = tweepy.API(auth)
#search tweets
tweets = api.search_tweets("####", tweet_mode="####")

for tweet in tweets:
    try:
        print(tweet.retweeted_status.full_text)
        print("=====")
    except AttributeError:
        print(tweet.full_text)
        print("=====")


        
