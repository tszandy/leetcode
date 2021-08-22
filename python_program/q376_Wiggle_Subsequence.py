from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
#use list instead of defaultdict a little faster
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        wiggle_sequence = [[1 for _ in range(n)] for _ in range(2)]
        
        for j in range(1,n):
            for i in range(j):
                if nums[i]<nums[j]:
                    wiggle_sequence[0][j] = max(wiggle_sequence[0][j],wiggle_sequence[1][i]+1)
                if nums[i]>nums[j]:
                    wiggle_sequence[1][j] = max(wiggle_sequence[1][j],wiggle_sequence[0][i]+1)
        return max(max(wiggle_sequence[0]),max(wiggle_sequence[1]))

# 
    def wiggleMaxLength_1(self, nums: List[int]) -> int:
        wiggle_sequence = [defaultdict(lambda:1,{}) for _ in range(2)]
        n = len(nums)
        wiggle_sequence[0][0]=1
        wiggle_sequence[1][0]=1
        
        for j in range(1,n):
            for i in range(j):
                if nums[i]<nums[j]:
                    wiggle_sequence[0][j] = max(wiggle_sequence[0][j],wiggle_sequence[1][i]+1)
                if nums[i]>nums[j]:
                    wiggle_sequence[1][j] = max(wiggle_sequence[1][j],wiggle_sequence[0][i]+1)
        return max(max(wiggle_sequence[0].values()),max(wiggle_sequence[1].values()))

sol = Solution()


# input
nums = [1,7,4,9,2,5]

# output
output = sol.wiggleMaxLength(nums)
# answer
answer = 6
print(output, answer, answer == output)

# input
nums = [1,17,5,10,13,15,10,5,16,8]

# output
output = sol.wiggleMaxLength(nums)
# answer
answer = 7
print(output, answer, answer == output)

# input
nums = [1,2,3,4,5,6,7,8,9]

# output
output = sol.wiggleMaxLength(nums)
# answer
answer = 2
print(output, answer, answer == output)

# input
nums = [0,0]

# output
output = sol.wiggleMaxLength(nums)
# answer
answer = 1
print(output, answer, answer == output)
