from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def divisorGame(self, n: int) -> bool:
        divisor_dp = [False]*(n+1)
        for j in range(1,n+1):
            for i in range(1,j):
                if j%i==0 and not divisor_dp[j-i]:
                    divisor_dp[j]=True
                    break
        return divisor_dp[n]

sol = Solution()


# input
n = 1
# output
output = sol.divisorGame(n)
# answer
answer = False
print(output, answer, answer == output)

# input
n = 100
# output
output = sol.divisorGame(n)
# answer
answer = True
print(output, answer, answer == output)

# input
n = 500
# output
output = sol.divisorGame(n)
# answer
answer = True
print(output, answer, answer == output)

# input
n = 1000
# output
output = sol.divisorGame(n)
# answer
answer = True
print(output, answer, answer == output)
