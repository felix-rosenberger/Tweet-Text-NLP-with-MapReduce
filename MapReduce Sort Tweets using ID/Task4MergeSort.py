#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 09:50:19 2022

@author: felixrosenbergernew
"""

from mrjob.job import MRJob

class MRMergeSort(MRJob): 

    def mapper(self, _, line):
        yield None, (int(line), 1)
            
    def reducer(self, _, values):
        # MapReduce uses MergeSort by default
        for i in sorted(values):
            yield i
            
if __name__ == '__main__': 
    MRMergeSort.run()