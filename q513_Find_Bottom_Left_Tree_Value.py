from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count
import queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.current_elem = None
        self.current_level = -1
        self.find_bottom_left(root,0)
        return self.current_elem

    def find_bottom_left(self,node,level):
        if node == None:
            return
        if self.current_level<level:
            self.current_level = level
            self.current_elem = node.val
        self.find_bottom_left(node.left,level+1)
        self.find_bottom_left(node.right,level+1)
        

sol = Solution()

# input
[2,null,3]
[2,1,3]
[1,2,3,4,null,5,6,null,null,7]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
