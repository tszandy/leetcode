from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        @lru_cache(None)
        def dp(n):
            if n ==1:
                return 0
            if n %2 == 0:
                return dp(n//2)+1
            if n %2 == 1:
                return dp(3*n+1)+1
        
        return sorted(list(range(lo,hi+1)),key = lambda x:(dp(x),x))[k-1]


sol = Solution()


# input
lo = 12

hi = 15

k = 2

# output
output = sol.getKth(lo,hi,k)
# answer
answer = 13
print(output, answer, answer == output)

# input
lo = 1

hi = 1

k = 1

# output
output = sol.getKth(lo,hi,k)
# answer
answer = 1
print(output, answer, answer == output)

# input
lo = 7

hi = 11

k = 4

# output
output = sol.getKth(lo,hi,k)
# answer
answer = 7
print(output, answer, answer == output)

# input
lo = 10

hi = 20

k = 5

# output
output = sol.getKth(lo,hi,k)
# answer
answer = 13
print(output, answer, answer == output)

# input
lo = 1

hi = 1000

k = 777

# output
output = sol.getKth(lo,hi,k)
# answer
answer = 570
print(output, answer, answer == output)
