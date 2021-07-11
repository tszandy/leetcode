from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [0]*(n+1)
        if n>=3:
            dp[1]=0
            dp[2]=1
            dp[3]=2
        else:
            return n-1
        for i in range(4,n+1):
            dp[i]=i-3+max(dp[i-4],i-1)
        return dp[n]        

sol = Solution()


# input
n = 1

# output
output = sol.getMoneyAmount(n)
# answer
answer = 0
print(output, answer, answer == output)

# input
n = 199

# output
output = sol.getMoneyAmount(n)
# answer
answer = 946
print(output, answer, answer == output)
