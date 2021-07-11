from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def integerReplacement(self, n: int) -> int:
        dp = {}
        dp[1]=0

        def integer_replacement(n):
            if n in dp:
                return dp[n]
            if n%2==0:
                dp[n] = integer_replacement(n//2)+1
                return dp[n]
            else:
                left = integer_replacement(n//2)
                right = integer_replacement(n//2+1)
                dp[n] = min(left,right)+2
                return dp[n]
        return integer_replacement(n)

sol = Solution()

# input
n = 1
# output
output = sol.integerReplacement(n)
# answer
answer = 0
print(output, answer, answer == output)

# input
n = 2
# output
output = sol.integerReplacement(n)
# answer
answer = 1
print(output, answer, answer == output)

# input
n = 3
# output
output = sol.integerReplacement(n)
# answer
answer = 2
print(output, answer, answer == output)

# input
n = 4
# output
output = sol.integerReplacement(n)
# answer
answer = 2
print(output, answer, answer == output)

# input
n = 7
# output
output = sol.integerReplacement(n)
# answer
answer = 4
print(output, answer, answer == output)

# input
n = 8
# output
output = sol.integerReplacement(n)
# answer
answer = 3
print(output, answer, answer == output)

# input
n = 42949672
# output
output = sol.integerReplacement(n)
# answer
answer = 32
print(output, answer, answer == output)

# input
n = 1074163236
# output
output = sol.integerReplacement(n)
# answer
answer = 37
print(output, answer, answer == output)
