from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        count = 0
        
        l = 0
        r = 1
        while l<r and r<n:
            if intervals[l][1]<=intervals[r][0]:
                l=r
                r+=1
            elif intervals[l][0]<intervals[r][0] and intervals[l][1]>intervals[r][1]:
                l=r
                r+=1
                count+=1
            else:
                r+=1
                count+=1
        return count

sol = Solution()


# input
intervals = [[1,2],[2,3],[3,4],[1,3]]
# output
output = sol.eraseOverlapIntervals(intervals)
# answer
answer = 1
print(output, answer, answer == output)

# input
intervals = [[1,2],[1,2],[1,2]]
# output
output = sol.eraseOverlapIntervals(intervals)
# answer
answer = 2
print(output, answer, answer == output)

# input
intervals = [[1,2],[2,3]]
# output
output = sol.eraseOverlapIntervals(intervals)
# answer
answer = 0
print(output, answer, answer == output)
