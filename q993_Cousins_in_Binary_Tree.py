from typing import List
from collections import Counter,defaultdict,deque
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count,zip_longest
import queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.node_x = None
        self.depth_x = None
        self.node_y = None
        self.depth_y = None
        self.find_cousin(root,x,y,0)
        if self.depth_x!=self.depth_y or self.node_x.par == self.node_y.par:
            return False
        else:
            return True
        
    def find_cousin(self,node,x,y,level,par=None):
        if node == None:
            return 
        node.par = par
        if node.val == x:
            self.node_x = node
            self.depth_x = level
        if node.val == y:
            self.node_y = node
            self.depth_y = level
        self.find_cousin(node.left,x,y,level+1,node)
        self.find_cousin(node.right,x,y,level+1,node)

sol = Solution()

# input
[1,2,3,4]
4
3
[1,2,3,null,4,null,5]
5
4
[1,2,3,null,4]
2
3
[1,2]
1
2
[1,2,3,7,null,8,null]
7
8

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
