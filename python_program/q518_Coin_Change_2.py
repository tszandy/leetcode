from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(key = lambda x:-x)
        
        return self.change_sub(amount,tuple(coins))
    
    @lru_cache(None)
    def change_sub(self,amount,coins):
        if len(coins)==0:
            return amount ==0
        largest_coin = coins[0]
        count = 0
        for i in range(amount//largest_coin+1)[::-1]:
            count+=self.change_sub(amount-i*largest_coin,coins[1:])
        return count

sol = Solution()

# input
amount = 5

coins = [1,2,5]

# output
output = sol.change(amount,coins)
# answer
answer = 4
print(output, answer, answer == output)

# input
amount = 6

coins = [1,2,5]

# output
output = sol.change(amount,coins)
# answer
answer = 5
print(output, answer, answer == output)

# input
amount = 105

coins = [1,2,5]

# output
output = sol.change(amount,coins)
# answer
answer = 594
print(output, answer, answer == output)

# input
amount = 3

coins = [2]

# output
output = sol.change(amount,coins)
# answer
answer = 0
print(output, answer, answer == output)

# input
amount = 10

coins = [10]

# output
output = sol.change(amount,coins)
# answer
answer = 1
print(output, answer, answer == output)
