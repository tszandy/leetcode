from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        if stones[1]!=1:
            return False

        k_index = defaultdict(set)
        stone_to_index = defaultdict(list)
        for i,e in enumerate(stones):
            stone_to_index[e].append(i)

        k_index[1] = set([1])
        for i in range(1,n):
            for k in k_index[i]:
                stone_1 = stones[i]+k+1
                stone_2 = stones[i]+k
                stone_3 = stones[i]+k-1
                
                if stone_1 in stone_to_index:
                    for index in stone_to_index[stone_1]:
                        if index>i:
                            k_index[index].add(k+1)
                if stone_2 in stone_to_index:
                    for index in stone_to_index[stone_2]:
                        if index>i:
                            k_index[index].add(k)
                if stone_3 in stone_to_index:
                    for index in stone_to_index[stone_3]:
                        if index>i:
                            k_index[index].add(k-1)
        if  len(k_index[n-1])!=0:
            return True
        else:
            return False
sol = Solution()


# input
stones = [0,1]

# output
output = sol.canCross(stones)
# answer
answer = True
print(output, answer, answer == output)

# input
stones = [0,2]

# output
output = sol.canCross(stones)
# answer
answer = False
print(output, answer, answer == output)

# input
stones = [0,1,2]

# output
output = sol.canCross(stones)
# answer
answer = True
print(output, answer, answer == output)

# input
stones = [0,1,3,5,6,8,12,17]

# output
output = sol.canCross(stones)
# answer
answer = True
print(output, answer, answer == output)

# input
stones = [0,1,2,3,4,8,9,11]

# output
output = sol.canCross(stones)
# answer
answer = False
print(output, answer, answer == output)
