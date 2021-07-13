from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def numTrees(self, n: int) -> int:
        dp={}
        dp[0]=1
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            count = 0
            for j in range(i):
                l = j
                r = i-1-j
                count+=dp[l]*dp[r]
            dp[i] = count
            
        return dp[n]
                

sol = Solution()


# input
n = 1

# output
output = sol.numTrees(n)
# answer
answer = 1
print(output, answer, answer == output)

# input
n = 2

# output
output = sol.numTrees(n)
# answer
answer = 2
print(output, answer, answer == output)

# input
n = 3

# output
output = sol.numTrees(n)
# answer
answer = 5
print(output, answer, answer == output)

# input
n = 19

# output
output = sol.numTrees(n)
# answer
answer = 1767263190
print(output, answer, answer == output)
