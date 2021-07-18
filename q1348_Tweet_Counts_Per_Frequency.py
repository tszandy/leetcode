from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class TweetCounts:

    def __init__(self):
        self.counter = Counter()

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.counter[(tweetName,time)]+=1

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        freq_to_num = {"minute":60,"hour":3600,"day":86400}
        return_list = []
        for i in range(startTime,endTime+1,freq_to_num[freq]):
            return_list.append(0)
            for j in range(min(freq_to_num[freq],endTime-i+1)):
                time = i+j
                return_list[-1]+=self.counter[(tweetName,time)]
        return return_list

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

sol = Solution()


# input
["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
