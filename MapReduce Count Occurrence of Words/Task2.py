#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program calculates the count of number of occurrences of each word in the text of tweets.
For this, the MapReduce framework is utilized to distribute the computing task on multiple machines.
"""

from mrjob.job import MRJob
import re

WORD_REGEXP = re.compile(r"[\w']+") # only words

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        words = WORD_REGEXP.findall(line) # take only words from input
        for word in words: 
            yield word.lower(), 1 # iterate over all words and output intermediate key,value pairs

    def reducer(self, key, values):
        yield key, sum(values) # take shuffled key,value pairs and sum the values for each key


if __name__ == '__main__':
    MRWordFrequencyCount.run()