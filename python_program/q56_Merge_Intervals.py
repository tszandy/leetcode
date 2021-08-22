from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
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

    def merge_1(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:(x[0],x[1]))
        
        elem_1 = intervals.pop(0)
        return_list = []
        while intervals:
            elem_2 = intervals.pop(0)
            if elem_2[0]<=elem_1[1]:
                if elem_1[1]<elem_2[1]:
                    elem_1 = [elem_1[0],elem_2[1]]
            else:
                return_list.append(elem_1)
                elem_1 = elem_2
        return_list.append(elem_1)
        return return_list

sol = Solution()


# input
intervals = [[1,3],[2,6],[8,10],[15,18]]

# output
output = sol.merge(intervals)
# answer
answer = [[1,6],[8,10],[15,18]]
print(output, answer, answer == output)

# input
intervals = [[1,4],[4,5]]

# output
output = sol.merge(intervals)
# answer
answer = [[1,5]]
print(output, answer, answer == output)
