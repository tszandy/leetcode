from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days.insert(0,0)
        n = len(days)
        
        dp = {0:0}
        for i in range(1,n):
            store_list = []
            if days[i]-1<=0:
                store_list.append(costs[0])
            else:
                store_list.append(dp[bisect_right(days,days[i]-1)-1]+costs[0])
            if days[i]-7<=0:
                store_list.append(costs[1])
            else:
                store_list.append(dp[bisect_right(days,days[i]-7)-1]+costs[1])
            if days[i]-30<=0:
                store_list.append(costs[2])
            else:
                store_list.append(dp[bisect_right(days,days[i]-30)-1]+costs[2])
            dp[i] = min(store_list)
        return dp[n-1]

sol = Solution()

# input
days = [1,4,6,7,8,20]

costs = [2,7,15]

# output
output = sol.mincostTickets(days,costs)
# answer
answer = 11
print(output, answer, answer == output)

# input
days = [1,2,3,4,5,6,7,8,9,10,30,31]

costs = [2,7,15]

# output
output = sol.mincostTickets(days,costs)
# answer
answer = 17
print(output, answer, answer == output)
