from typing import List
from collections import Counter,defaultdict,deque
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count,zip_longest
import queue

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        count_jewels = 0
        for stone in stones:
            if stone in jewels_set:
                count_jewels+=1
        return count_jewels

sol = Solution()

# input
jewels = "aA"

stones = "aAAbbbb"

# output
output = sol.numJewelsInStones(jewels,stones)
# answer
answer = 3
print(output, answer, answer == output)

# input
jewels = "z"

stones = "ZZ"

# output
output = sol.numJewelsInStones(jewels,stones)
# answer
answer = 0
print(output, answer, answer == output)
