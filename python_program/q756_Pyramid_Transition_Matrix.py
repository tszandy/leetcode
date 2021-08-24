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
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        pyramid_map = defaultdict(set)
        for block in allowed:
            pyramid_map[block[:2]].add(block[2])
        bottom = list(map(lambda x:set([x]),list(bottom)))
        n = len(bottom)
        for i in range(n)[::-1]:
            for j in range(i):
                new_set = set()
                for char_1 in bottom[j]:
                    for char_2 in bottom[j+1]:
                        new_set = new_set.union(pyramid_map[char_1+char_2])
                bottom[j] = new_set
        return len(bottom[0])!=0

sol = Solution()

# input
bottom = "BCD"

allowed = ["BCG","CDE","GEA","FFF"]

# output
output = sol.pyramidTransition(bottom,allowed)
# answer
answer = True
print(output, answer, answer == output)

# input
bottom = "AABA"

allowed = ["AAA","AAB","ABA","ABB","BAC"]

# output
output = sol.pyramidTransition(bottom,allowed)
# answer
answer = False
print(output, answer, answer == output)
