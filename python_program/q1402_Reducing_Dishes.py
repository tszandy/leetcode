from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        dp = defaultdict(int)
        n = len(satisfaction)
        
        for t in range(1,n+1):
            max_list = []
            if t>=2:
                max_list.append(dp[t-2,t-1])
            for s in range(t-1,n):
                if t ==1:
                    dp[s,t] = satisfaction[s]*t
                else:
                    dp[s,t] = max(max_list)+satisfaction[s]*t
                max_list.append(dp[s,t-1])
        return max(dp.values())

sol = Solution()


# input
satisfaction = [-1,-8,0,5,-9]

# output
output = sol.maxSatisfaction(satisfaction)
# answer
answer = 14
print(output, answer, answer == output)

# input
satisfaction = [4,3,2]

# output
output = sol.maxSatisfaction(satisfaction)
# answer
answer = 20
print(output, answer, answer == output)

# input
satisfaction = [-1,-4,-5]

# output
output = sol.maxSatisfaction(satisfaction)
# answer
answer = 0
print(output, answer, answer == output)

# input
satisfaction = [-2,5,-1,0,3,-3]

# output
output = sol.maxSatisfaction(satisfaction)
# answer
answer = 35
print(output, answer, answer == output)
