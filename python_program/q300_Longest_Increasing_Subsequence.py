from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = bisect_left(sub,num)
            
            if i == len(sub):
                sub.append(num)
            else:
                sub[i]=num
        return len(sub)
    
    def lengthOfLIS_1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        dp[0]=1
        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
                    
        return max(dp)
    

sol = Solution()


# input
nums = [10,9,2,5,3,7,101,18]

# output
output = sol.lengthOfLIS(nums)
# answer
answer = 4
print(output, answer, answer == output)

# input
nums = [0,1,0,3,2,3]

# output
output = sol.lengthOfLIS(nums)
# answer
answer = 4
print(output, answer, answer == output)

# input
nums = [7,7,7,7,7,7,7]

# output
output = sol.lengthOfLIS(nums)
# answer
answer = 1
print(output, answer, answer == output)
