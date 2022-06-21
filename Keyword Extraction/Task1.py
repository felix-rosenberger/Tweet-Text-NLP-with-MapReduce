#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program:
    1. reads data in from MongoDB
    2. Tokenizes and removes stopwords from each tweet's text
    3. Extracts keywords from the text of each tweet
    4. Stores the keywords into a CSV file
    5. Updates the original tweets in the MongoDB by adding a "keyword" tag into each document with the keyword:POS pairs as values
"""
#library import
from pymongo import MongoClient #responsible for database connection
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

# Read data in
client = MongoClient('127.0.0.1', 27017) # ip and port number
db = client["Assignment1"] # db name
tweets = db["TweetsAssignment"] # collection name

# define function for word tokenization
def text_tokenize(text):
    """This function takes a string as input and returns a list of words as output."""
    tokenized_text = word_tokenize(text)
    return tokenized_text

# define function for stopwords
def remove_stopwords(words):
    """This function takes a list of words as input and returns a list of words without stopwords."""
    english_stopwords = stopwords.words('english')
    result = []
    for word in words:
        if word not in english_stopwords:
            result.append(word)
    return result

# define function to create the list of text where keywords can be extracted from
def list_of_words(text):
    """This function takes a string as input and returns a list of english words."""
    text = re.sub(r"[^\w]"," ", text) # removes non-alphabetical symbols
    words = text_tokenize(text) # takes string and tokenizes it into list of words
    no_stopwords = remove_stopwords(words) # takes tokenized list and removes stopwords
    return no_stopwords

# define csv function
def keywords_to_csv(keywords):
    """This function takes a list of words and outputs a comma separated string."""
    for k in keywords:
        global string # otherwise referenced before assignment
        string = ",".join([str(i) for i in keywords])
    return string

# extract words from the text field of the tweets using the functions from above and update the original tweet with a new field
for tweet in tweets.find():
    if 'body' in tweet.keys(): # to check for existence of key and only perform if existent
        keywords = list_of_words(tweet["body"])
        string = keywords_to_csv(keywords)
        if 'actor' in tweet.keys():
            tweets.update_many({"actor.id":tweet["actor"]["id"]}, {"$set":{"keyword":string}})

        

        