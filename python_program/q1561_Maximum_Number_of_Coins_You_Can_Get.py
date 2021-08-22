from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles = sorted(piles)[n//3:]
        count_coin = 0
        for i,e in enumerate(piles):
            if i%2 == 0:
                count_coin += e
        return count_coin

sol = Solution()


# input
piles = [2,4,1,2,7,8]
# output
output = sol.maxCoins(piles)
# answer
answer = 9
print(output, answer, answer == output)

# input
piles = [2,4,5]
# output
output = sol.maxCoins(piles)
# answer
answer = 4
print(output, answer, answer == output)

# input
piles = [9,8,7,6,5,1,2,3,4]
# output
output = sol.maxCoins(piles)
# answer
answer = 18
print(output, answer, answer == output)

# input
piles = [9,8,7,6,5,1,2,3,4,32,1,2,51,2,3,654,4,3,5434,643,234]
# output
output = sol.maxCoins(piles)
# answer
answer = 941
print(output, answer, answer == output)
