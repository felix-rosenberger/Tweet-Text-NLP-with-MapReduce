#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 15:06:25 2022

@author: felixrosenbergernew
"""

import pandas as pd
from pymongo import MongoClient #responsible for database connection

client = MongoClient('127.0.0.1', 27017) # ip and port number, could be cloud url
db = client["Assignment1"] # db name
tweets = db["TweetsAssignment"] # collection name

TweetCities = []
try:
    for tweet in tweets.find():
        TweetCities.append(tweet["actor"]["twitterTimeZone"])
except KeyError:
    print(None)

print(TweetCities[:10])

# write list to dataframe
df = pd.DataFrame(TweetCities)
print(df[0:10])

# read in australian city names and write them to a list for later removal of non-australian cities
australiacities = pd.read_csv("au.csv", header = None)
australia = australiacities[0].tolist()

# remove all values that are not in the list of australian cities
df = df[df[0].isin(australia)]
print(df[:10])

df.to_csv("Task3Input.txt", header = None, index = None)

