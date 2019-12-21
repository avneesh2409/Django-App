import tweepy 
  
# Fill the X's with the credentials obtained by  
# following the above mentioned procedure. 
consumer_key = "OT27TTlLY4vvIwB2EefPAL9uQ" 
consumer_secret = "fClFbh0aVJ49f8fYPIuC6aUFFo8Q8USZCmVzlQpFSg6xZQldVS"
access_key = "759322066461925376-BFVvZwcH7X5pnLgrOdbJBuSQtMybh9t"
access_secret = "2Yl1pfCaeRgFL59CfycLun7D1QHE8XvcpLUFHLkPLf8zR"
  
# Function to extract tweets 
def get_tweets(username): 
          
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 
        user = api.me()
        #api.update_status('Hello Python Central!')
        # 200 tweets to be extracted 
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username) 
        tmp=[]  
        tweets_for_csv = [tweet.text for tweet in tweets] 
        for j in tweets_for_csv: 
        	tmp.append(j)  
        return tmp
 
