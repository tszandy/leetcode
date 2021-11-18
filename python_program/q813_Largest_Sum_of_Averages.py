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
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        self.n = len(nums)
        self.nums = nums
        return self.dp(0,k)
        
    @lru_cache(None)
    def dp(self,i,k):
        if k==1:
            return self.average(self.nums[i:])
        max_score = 0
        for j in range(i+1,self.n-1-(k-3)):
            max_score = max(max_score,self.average(self.nums[i:j])+self.dp(j,k-1))
        return max_score

    def average(self,arr):
        return sum(arr)/len(arr)

sol = Solution()

# input
nums = [9,1,2,3,9,1,2,3,4,1,4,21,4,69,2,3,3,2,15,1,32,2,3,1,70,5,2,3,2,2,1,1,5,2,1,45]

k = 20

# output
output = sol.largestSumOfAverages(nums,k)
# answer
answer = 303.53333

print(output, answer, answer == output)

# input
nums = [1,2,3,4,5,6,7]

k = 4

# output
output = sol.largestSumOfAverages(nums,k)
# answer
answer = 20.50000

print(output, answer, answer == output)

# input
nums = [9,1,2,3,9]

k = 3

# output
output = sol.largestSumOfAverages(nums,k)
# answer
answer = 20.50000

print(output, answer, answer == output)
