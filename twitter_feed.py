import csv
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Stream
from tweepy.streaming import StreamListener

TWITTER_APP_KEY = 'QzZvmRaTAJUkjPdSAkeGxr9eO'
TWITTER_APP_SECRET = '1iMQrEK4gPnzx7pjRk1SpAqdNlGNYzAo2DAzIr0V9NH3fMWEAu'
TWITTER_KEY = '1019156295260278784-lBCIH1xiOv0MWg5tAZtyHuzAzDywMR'
TWITTER_SECRET = 'Vuso2iMcUs4MKNMgIDYTOKQIH29M1nhUu5F9bxjULCfv6'


auth = OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_SECRET)
auth.set_access_token(TWITTER_KEY, TWITTER_SECRET)

api = API(auth)


class StreamListener(StreamListener):

    # Subclassing StreamListener class
    # used to keep up with when users post tweets

    def on_status(self, status):
        print(status.text)
        # loc = status.user.location
        # print('loc:',status.user.location)
        # new_log = open('tweet.csv', 'a')
        # writer = csv.writer(new_log)
        # writer.writerow([loc])



    #error handling, code sent if rate limited

    def on_error(self,status_code):
        print(status_code)


    def on_data(self,data):
        print(data)
        x = data.split('"')
        time = x[3]
        tweet = x[13]
        twitter_handle = x[49]
        loc = x[53]

        #print(twitter_handle)





        new_log = open('tweet.csv', 'a')
        writer = csv.writer(new_log,dialect='unix')
        writer.writerow([time,loc,twitter_handle,tweet])
        return True

stream_listener = StreamListener()
stream = Stream(api.auth,stream_listener)
stream.filter(track=['football'])

