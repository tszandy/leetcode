from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def get_money_amount(l,r):
            if r<=l:
                return 0           
            min_amount = float("inf")
            for k in range(l,r+1):
                min_amount = min(min_amount,max(get_money_amount(l,k-1),get_money_amount(k+1,r))+k)
            return min_amount
        return get_money_amount(1,n)
                
sol = Solution()


# input
n = 1

# output
output = sol.getMoneyAmount(n)
# answer
answer = 0
print(output, answer, answer == output)

# input
n = 149

# output
output = sol.getMoneyAmount(n)
# answer
answer = 686
print(output, answer, answer == output)

# input
n = 199

# output
output = sol.getMoneyAmount(n)
# answer
answer = 946
print(output, answer, answer == output)
