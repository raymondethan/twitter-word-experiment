#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, API, Cursor, models
from tweepy import Stream
import json
from datetime import datetime
import time
from time import mktime

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

# Status() is the data model for a tweet
models.Status.first_parse = models.Status.parse
models.Status.parse = parse
# User() is the data model for a user profil
models.User.first_parse = models.User.parse
models.User.parse = parse
# You need to do it for all the models you need

#Variables that contains the user credentials to access Twitter API
access_token = "1531939002-pzqvq9p1sipGlfOvNSZtjYcickMxkvE14Hpm8K3"
access_token_secret = "5sZNztO5c7TrRK4ezpTFdonNaxcjhkimwNvCX181Q2IIe"
consumer_key = "sSAyiHdPGo7SnFerZA4BdYPY2"
consumer_secret = "pXkqhbHBDOkG7Cor7AWkpq5yRA1RWjKxFv1KKtS3ejQ58JdvSF"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    
    def on_data(self, data):
        #print("success")
        return True
    
    def on_error(self, status):
        #print("error")
        print(status)

class myStreamListener(StreamListener):

    def on_data(self, data):
        try:
            with open('tufts.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = API(auth)
#    for tweet in Cursor(api.user_timeline).items(1):
#        print(tweet.json)

    tufts = {"lng1":-71.126261, "lat1":42.403836,"lng2":-71.110554,"lat2":42.414356}
    vandy = {"lat1":36.137818,"lng1":-86.813750,"lat2":36.151369,"lng2":-86.797485}
    twitter_stream = Stream(auth, myStreamListener())

    twitter_stream.filter(locations=[tufts["lng1"],tufts["lat1"],tufts["lng2"],tufts["lat2"]])

    
    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
#stream.filter(track=['python', 'javascript', 'ruby'])