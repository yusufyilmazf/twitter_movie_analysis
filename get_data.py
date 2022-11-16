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


results =  tweepy_api.search_tweets(q="Hashtag Name", lang="tr",count=3, result_type="recent")
for tweet in results:
    print("=====START=====")
    print ("Number of Tweet  : ",tweet_number) 
    print ("Twitter UserName : ",tweet.user.screen_name)
    print ("=====================")
    print ("Tweet Contets : ",tweet.text)
    print ("=====================")
    print ("Created Time : ",tweet.created_at)
    print ("=====================")
    print ("Like count : ",tweet.favorite_count)
    print ("=====================")
    print ("Retweet count : ",tweet.retweet_count)
    print ("=====================")
    print ("Tweeet Source  : ",tweet.source)
    print ("=====================")
    print ("Tweet Language : ",tweet.lang)
    print ("=======END OF TWEET=======")
    print ("  ")


        
