from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==2:
            return 0
        n = len(cost)
        total_min_cost_array = [0]*(n+1)

        for i in range(2,n+1):
            total_min_cost_array[i] = min(total_min_cost_array[i-2]+cost[i-2],total_min_cost_array[i-1]+cost[i-1])
        return total_min_cost_array[-1]

sol = Solution()


# input
cost = [1,2]
# output
output = sol.minCostClimbingStairs(cost)
# answer
answer = 1
print(output, answer, answer == output)

# input
cost = [2,1]
# output
output = sol.minCostClimbingStairs(cost)
# answer
answer = 1
print(output, answer, answer == output)

# input
cost = [10,15,20]
# output
output = sol.minCostClimbingStairs(cost)
# answer
answer = 15
print(output, answer, answer == output)

# input
cost = [1,100,1,1,1,100,1,1,100,1]
# output
output = sol.minCostClimbingStairs(cost)
# answer
answer = 6
print(output, answer, answer == output)

# input
cost = [1,100,1,1,1,100,1,1,100,1,1,2,10,5,1,2,3,5,64,2,3,54,1,2,3,41,321,32,4,1,231,321,321,3,32,21,859]
# output
output = sol.minCostClimbingStairs(cost)
# answer
answer = 447
print(output, answer, answer == output)
