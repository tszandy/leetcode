from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        return self.merge(intervals)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:(x[0],x[1]))
        
        elem_1 = intervals.pop(0)
        i = 0
        while i<len(intervals):
            elem_2 = intervals.pop(i)
            if elem_2[0]<=elem_1[1]:
                if elem_1[1]<elem_2[1]:
                    elem_1 = [elem_1[0],elem_2[1]]
            else:
                intervals.insert(i,elem_1)
                i+=1
                elem_1 = elem_2
        intervals.insert(i,elem_1)
        return intervals


sol = Solution()


# input
intervals = [[1,3],[6,9]]

newInterval = [2,5]

# output
output = sol.insert(intervals, newInterval)
# answer
answer = [[1,5],[6,9]]
print(output, answer, answer == output)

# input
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]

newInterval = [4,8]

# output
output = sol.insert(intervals, newInterval)
# answer
answer = [[1,2],[3,10],[12,16]]
print(output, answer, answer == output)

# input
intervals = []

newInterval = [5,7]

# output
output = sol.insert(intervals, newInterval)
# answer
answer = [[5,7]]
print(output, answer, answer == output)

# input
intervals = [[1,5]]

newInterval = [2,3]

# output
output = sol.insert(intervals, newInterval)
# answer
answer = [[1,5]]
print(output, answer, answer == output)

# input
intervals = [[1,5]]

newInterval = [2,7]

# output
output = sol.insert(intervals, newInterval)
# answer
answer = [[1,7]]
print(output, answer, answer == output)
