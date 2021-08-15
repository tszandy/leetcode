from typing import List
from collections import Counter,defaultdict,deque
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count,zip_longest
import queue

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        self.grid = grid
        n = len(grid)
        return self.construct_1(0,n-1,0,n-1)
        
        
    def construct_1(self,l,r,t,d):
        if r - l ==0:
            return Node(val = self.grid[t][l],isLeaf = True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
        else:
            topLeft = self.construct_1(l,(l+r)//2,t,(t+d)//2)
            topRight = self.construct_1((l+r)//2+1,r,t,(t+d)//2)
            bottomLeft = self.construct_1(l,(l+r)//2,(t+d)//2+1,d)
            bottomRight = self.construct_1((l+r)//2+1,r,(t+d)//2+1,d)
            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                return Node(val = topLeft.val,isLeaf = True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            else:
                return Node(val = topLeft.val,isLeaf = False, topLeft=topLeft, topRight=topRight, bottomLeft=bottomLeft, bottomRight=bottomRight)

sol = Solution()

# input
[[0,1],[1,0]]
[[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
[[1,1],[1,1]]
[[0]]
[[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
