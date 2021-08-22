from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        M = 1
        return self.alice_pick(M,tuple(piles))
    
    @lru_cache(None)
    def alice_pick(self,M,piles):
        if len(piles)==0:
            return 0 
        max_list = []
        for i in range(1,2*M+1):
            max_list.append(sum(piles[:i])+self.bob_pick(max(M,i),piles[i:]))
        return max(max_list)
    
    @lru_cache(None)
    def bob_pick(self,M,piles):
        if len(piles)==0:
            return 0 
        min_list = []
        for i in range(1,2*M+1):
            min_list.append(self.alice_pick(max(M,i),piles[i:]))
        return min(min_list)


sol = Solution()

# input
piles = [2,7,9,4,4]

# output
output = sol.stoneGameII(piles)
# answer
answer = 10
print(output, answer, answer == output)

# input
piles = [1,2,3,4,5,100]

# output
output = sol.stoneGameII(piles)
# answer
answer = 104
print(output, answer, answer == output)
