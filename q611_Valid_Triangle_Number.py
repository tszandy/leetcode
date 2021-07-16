from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n-1,1,-1):
            l = 0
            r = i-1

            while(l<r):
                if nums[l]+nums[r] >nums[i]:
                    count+=r-l
                    r -=1
                else:
                    l +=1
                    
        return count

sol = Solution()


# input
nums = [2,2,3,4]

# output
output = sol.triangleNumber(nums)
# answer
answer = 3
print(output, answer, answer == output)

# input
nums = [4,2,3,4]

# output
output = sol.triangleNumber(nums)
# answer
answer = 4
print(output, answer, answer == output)
