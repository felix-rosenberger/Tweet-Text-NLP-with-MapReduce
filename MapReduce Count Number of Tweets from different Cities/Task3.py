#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 15:13:40 2022

@author: felixrosenbergernew
"""
from mrjob.job import MRJob
import re

WORD_REGEXP = re.compile(r"[\w']+") # only words

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        words = WORD_REGEXP.findall(line) # take only words from input
        for word in words: 
            yield word, 1 # iterate over all words and output intermediate key,value pairs

    def reducer(self, key, values):
        yield key, sum(values) # take shuffled key,value pairs and sum the values for each key


if __name__ == '__main__':
    MRWordFrequencyCount.run()