#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 09:25:57 2022

@author: felixrosenbergernew
"""

from pymongo import MongoClient #responsible for database connection

client = MongoClient('127.0.0.1', 27017) # ip and port number, could be cloud url
db = client["Assignment1"] # db name
tweets = db["TweetsAssignment"] # collection name


TweetIDs = []
try:
    for tweet in tweets.find():
        TweetIDs.append(tweet["id"][-18:])
except KeyError:
    print(None)
    
print(len(TweetIDs))
print(TweetIDs[:9])

textfile = open("Task4Input.txt", "w")
for element in TweetIDs:
    textfile.write(element + "\n")
textfile.close()