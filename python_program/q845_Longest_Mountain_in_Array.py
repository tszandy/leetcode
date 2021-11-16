from typing import List
from collections import Counter,defaultdict,deque
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count,zip_longest
import queue

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        left_mountain = [1]*n
        for index in range(1,n):
            if arr[index-1]<arr[index]:
                left_mountain[index] = left_mountain[index-1]+1
        right_mountain = [1]*n
        for index in range(n-1)[::-1]:
            if arr[index]>arr[index+1]:
                right_mountain[index] = right_mountain[index+1]+1
        max_mountain = 0
        for index in range(n):
            if left_mountain[index]!=1 and right_mountain[index]!=1:
                max_mountain = max(max_mountain,left_mountain[index]+right_mountain[index]-1)
        return 0 if max_mountain<3 else max_mountain

sol = Solution()

# input
arr = [2,1,4,7,3,2,5]

# output
output = sol.longestMountain(arr)
# answer
answer = 5

print(output, answer, answer == output)

# input
arr = [2,2,2]

# output
output = sol.longestMountain(arr)
# answer
answer = 0

print(output, answer, answer == output)

# input
arr = [0,1,2,3,4,5,6,7,8,9]

# output
output = sol.longestMountain(arr)
# answer
answer = 0

print(output, answer, answer == output)
