from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = defaultdict(list)
        for i in range(n):
            dp[i].append(nums[i])
        for i in range(1,n):
            for j in range(i):
                num_1,num_2 = nums[j],nums[i]
                if num_2%num_1 == 0:
                    if len(dp[j])>len(dp[i])-1:
                        dp[i] = dp[j]+[nums[i]]
        max_len = reduce(max,map(lambda x:len(x),dp.values()))
        for value in dp.values():
            if len(value)==max_len:
                return value

sol = Solution()


# input
nums = [1,2,3]

# output
output = sol.largestDivisibleSubset(nums)
# answer
answer = [1,2]
print(output, answer, answer == output)

# input
nums = [1,2,4,8]

# output
output = sol.largestDivisibleSubset(nums)
# answer
answer = [1,2,4,8]
print(output, answer, answer == output)
