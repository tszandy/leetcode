from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count
import queue

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        self.max_depth_count = 0
        self.max_depth(root,1)
        return self.max_depth_count

    def max_depth(self,node,level):
        self.max_depth_count = max(self.max_depth_count,level)
        for c in node.children:
            self.max_depth(c,level+1)


sol = Solution()

# input
[1,null,3,2,4,null,5,6]
[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
