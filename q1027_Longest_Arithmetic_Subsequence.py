from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        longest_ari_sub = [defaultdict(lambda :1) for _ in range(n)]
        
        for j in range(1,n):
            y = nums[j]
            for i in range(j):
                x = nums[i]
                longest_ari_sub[j][y-x] = longest_ari_sub[i][y-x]+1
        
        return max(map(lambda x:max(x.values()),longest_ari_sub))

sol = Solution()


# input
nums = [3,6,9,12]

# output
output = sol.longestArithSeqLength(nums)
# answer
answer = 4
print(output, answer, answer == output)

# input
nums = [9,4,7,2,10]

# output
output = sol.longestArithSeqLength(nums)
# answer
answer = 3
print(output, answer, answer == output)

# input
nums = [20,1,15,3,10,5,8]

# output
output = sol.longestArithSeqLength(nums)
# answer
answer = 4
print(output, answer, answer == output)