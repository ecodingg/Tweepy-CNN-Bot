import tweepy

consumerKey = 'Replace'
consumerSecret = 'Replace'
accessToken = 'Replace'
accessTokenSecret = 'Replace'
bearerToken = 'Replace'

api = tweepy.Client(bearer_token = bearerToken,
              consumer_key = consumerKey,
              consumer_secret = consumerSecret,
              access_token = accessToken,
              access_token_secret = accessTokenSecret)

def tweet(text):
    api.create_tweet(text=text, user_auth=True)

