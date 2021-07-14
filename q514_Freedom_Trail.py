from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        char_to_index = defaultdict(list)
        for i,c in enumerate(ring):
            char_to_index[c].append(i)
        n = len(ring)
        answer_list = [(0,0)]
        for c in key:
            next_list = []
            for index_1 in char_to_index[c]:
                min_step = float('inf')
                for index_2,step in answer_list:
                    min_step = min(min_step,step+min((index_1-index_2)%n,(index_2-index_1)%n)+1)
                new_index = index_1
                next_list.append((new_index,min_step))
            answer_list = next_list

        min_step = float('inf')
        for _ ,step in answer_list:
            min_step = min(min_step,step)
            
        return min_step

sol = Solution()


# input
ring = "godding"
key = "gd"
# output
output = sol.findRotateSteps(ring,key)
# answer
answer = 4
print(output, answer, answer == output)

# input
ring = "godding"
key = "godding"
# output
output = sol.findRotateSteps(ring,key)
# answer
answer = 13
print(output, answer, answer == output)

# input
ring = "godding"
key = "goddinggoddinggoddin"
# output
output = sol.findRotateSteps(ring,key)
# answer
answer = 39
print(output, answer, answer == output)

# input
ring = "godding"
key = "goddinggoddingoddinggoddiggoddingoddinggoddingoddinggoddiggoddingoddinggoddingoddinggoddiggoddin"
# output
output = sol.findRotateSteps(ring,key)
# answer
answer = 199
print(output, answer, answer == output)
