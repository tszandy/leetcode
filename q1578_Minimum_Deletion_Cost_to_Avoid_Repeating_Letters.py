from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        count_cost = 0
        n = len(s)
        pre_c = None
        pre_cost_c = 0
        for i in range(n):
            c = s[i]
            cost_c = cost[i]
            if c!=pre_c:
                pre_c = c
                pre_cost_c = cost_c
                continue
            else:
                count_cost+= min(pre_cost_c,cost_c)
                pre_cost_c = max(pre_cost_c,cost_c)
        return count_cost


sol = Solution()

# input
s = "abaac"

cost = [1,2,3,4,5]

# output
output = sol.minCost(s,cost)
# answer
answer = 3
print(output, answer, answer == output)

sol = Solution()

# input
s = "abc"

cost = [1,2,3]

# output
output = sol.minCost(s,cost)
# answer
answer = 0
print(output, answer, answer == output)

sol = Solution()

# input
s = "aabaa"

cost = [1,2,3,4,1]

# output
output = sol.minCost(s,cost)
# answer
answer = 2
print(output, answer, answer == output)
