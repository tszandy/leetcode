from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n<=1:
            return n
            
        nums = [0]*(n+1)
        nums[1]=1
        for i in range(n+1):
            if i %2==0:
                nums[i]=nums[i//2]
            else:
                nums[i]=nums[i//2]+nums[i//2+1]
        return max(nums)


sol = Solution()


# input
n = 0
# output
output = sol.getMaximumGenerated(n)
# answer
answer = 0
print(output, answer, answer == output)

# input
n = 1
# output
output = sol.getMaximumGenerated(n)
# answer
answer = 1
print(output, answer, answer == output)

# input
n = 100
# output
output = sol.getMaximumGenerated(n)
# answer
answer = 21
print(output, answer, answer == output)
