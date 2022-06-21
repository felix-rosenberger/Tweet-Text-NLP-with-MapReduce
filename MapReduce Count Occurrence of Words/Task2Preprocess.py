#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 11:49:12 2022

@author: felixrosenbergernew
"""

import pandas as pd
from pymongo import MongoClient #responsible for database connection

client = MongoClient('127.0.0.1', 27017) # ip and port number, could be cloud url
db = client["Assignment1"] # db name
tweets = db["TweetsAssignment"] # collection name

TweetText = []
try:
    for tweet in tweets.find():
        TweetText.append(tweet["body"])
except KeyError:
    print(None)
    
print(TweetText[:10])

# write list to dataframe
df = pd.DataFrame(TweetText)
print(df[:10])
# save as txt file
df.to_csv("Task2Input.txt", header = None, index = None)

