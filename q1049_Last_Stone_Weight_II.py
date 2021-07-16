from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        sum_stones = sum(stones) 
        half = sum_stones//2
        tile_of_stones = set([0])
        
        for i in range(n):
            next_tile = set()            
            stone = stones[i]
            if stone <=half:
                next_tile.add(stone)
            for weight in tile_of_stones:
                next_tile.add(weight)
                if weight+stone<=half and weight+stone not in tile_of_stones:
                    next_tile.add(weight+stone)
            for weight in next_tile:
                tile_of_stones.add(weight)

        max_tile = max(tile_of_stones)
        return sum_stones-2*max_tile

sol = Solution()


# input
stones = [91]
# output
output = sol.lastStoneWeightII(stones)
# answer
answer = 91
print(output, answer, answer == output)

# input
stones = [2,7,4,1,8,1]
# output
output = sol.lastStoneWeightII(stones)
# answer
answer = 1
print(output, answer, answer == output)

# input
stones = [31,26,33,21,40]
# output
output = sol.lastStoneWeightII(stones)
# answer
answer = 5
print(output, answer, answer == output)

# input
stones = [1,2]
# output
output = sol.lastStoneWeightII(stones)
# answer
answer = 1
print(output, answer, answer == output)
