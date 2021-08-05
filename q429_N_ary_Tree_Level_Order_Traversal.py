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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []
        self.store_list = []
        self.level_order(root,0)
        return self.store_list
    def level_order(self,node,level):
        if len(self.store_list)<=level:
            self.store_list.append([])
        self.store_list[level].append(node.val)
        for next_level_node in node.children:
            self.level_order(next_level_node,level+1)


sol = Solution()

# input
[1,null,3,2,4,null,5,6]
[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

# output
output = sol.levelOrder(root)
# answer
answer = ""
print(output, answer, answer == output)
