from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.n = len(nums)
        memo = [defaultdict(lambda :float("-inf")) for _ in range(self.n)]
        return self.calculate(nums,0,0,target,memo)
    def calculate(self,nums,i,sum_num,target,memo):
        if i == self.n:
            if sum_num == target:
                return 1
            else:
                return 0
        else:
            if memo[i][sum_num]!=float("-inf"):
                return memo[i][sum_num]
            add = self.calculate(nums,i+1,sum_num+nums[i],target,memo)
            subtract = self.calculate(nums,i+1,sum_num-nums[i],target,memo)
            memo[i][sum_num] = add+subtract
            return memo[i][sum_num]

sol = Solution()

# input
nums = [1,1,1,1,1]

target = 3

# output
output = sol.findTargetSumWays(nums,target)
# answer
answer = 5
print(output, answer, answer == output)

# input
nums = [1]

target = 1

# output
output = sol.findTargetSumWays(nums,target)
# answer
answer = 1
print(output, answer, answer == output)
