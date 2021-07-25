from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if all(row[j]<=row[i] for row in strs):
                    dp[i] = max(dp[i],1+dp[j])
        return n-max(dp)

sol = Solution()

# input
strs = ["babca","bbazb"]

# output
output = sol.minDeletionSize(strs)
# answer
answer = 3
print(output, answer, answer == output)

# input
strs = ["edcba"]

# output
output = sol.minDeletionSize(strs)
# answer
answer = 4
print(output, answer, answer == output)

# input
strs = ["ghi","def","abc"]

# output
output = sol.minDeletionSize(strs)
# answer
answer = 0
print(output, answer, answer == output)
