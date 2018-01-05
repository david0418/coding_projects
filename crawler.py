# -*- coding: utf-8 -*-
import tweepy
from time import *


#consumer key, consumer secret, access token, access secret.
ckey="jHP4lfhWRwM7Nr3frBuz5is51"
csecret="rWuo44lGBrd9eIFFNEIkpA7t2cSn9WEHjaoSblo0lD74YVagsb"
atoken="948795124691099648-3qhNBAaWrhw61BJVWibZeYvejsa26yA"
asecret="SUts7Xdr1xyGxLHOr9x24rVsNHE512RVflRjpAa1yhQ6a"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
aois = ['CGTNOfficial','AP','Reuters','AFP','CNN','RT_com']

def news_update():
    count = 0
    while count <= 2:
        count+=1
        print ctime()
        for aoi in aois:
            print aoi
            i = 0
            stuff = api.user_timeline(screen_name = aoi, count = 5, include_rts = True, tweet_mode="extended")
            for status in stuff:
                i += 1
                print str(i) + '. ' +status._json['full_text'].split('http')[0]
            print '\n\n\n'
        sleep(5)

if __name__ == "__main__":
    news_update()
