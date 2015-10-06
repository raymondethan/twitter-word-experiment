from instagram.client import InstagramAPI
from random import randint
import sys
import time
from collections import OrderedDict
from datetime import datetime,timedelta
from urllib import request

#('2179392322.7ab1c9e.3ef6054ce1164186a54dfd15e760e242', {'id': '2179392322', 'profile_picture': 'https://instagramimages-a.akamaihd.net/profiles/anonymousUser.jpg', 'website': '', 'username': 'eraybert14', 'full_name': 'Ethan Raymond', 'bio': ''})
access_token = "2179392322.7ab1c9e.3ef6054ce1164186a54dfd15e760e242"
client_secret = "d5f70799202941d4aa928b6f1222a19a"
api = InstagramAPI(access_token=access_token, client_secret=client_secret)
photos = []
minDate = datetime(2015,8,15)
mS = api.media_search(lat='36.145214',lng='-86.806653',distance=5000)
photos = [photo for photo in mS]
for photo in photos:
    print(photo.tags)

#while minDate <= datetime.today():
#    nextDay = minDate + timedelta(1)
#    mediaSearch = api.media_search(lat='36.145214',lng='-86.806653',min_timestamp=minDate,max_timestamp=nextDay,distance=5000)
#    print(len(mediaSearch),len(photos))
#    for photo in mediaSearch:
#        photos.append(photo)
#    minDate = nextDay
#
#rootUser = api.user_followed_by()
##print(rootUser)
##photos = []
#print(len(photos))
#outfile.write("Taken_by\tTagged\tCaption")
#with open("data.txt") as outfile:
#    for photo in photos:
#        outfile.write(photo.user.username + '\t' +
#    print(i)