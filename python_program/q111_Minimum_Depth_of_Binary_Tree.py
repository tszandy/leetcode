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
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.count_min = float("inf")
        self.min_depth(root,1)
        return self.count_min

    def min_depth(self,node,level):
        if node.left == node.right == None:
            self.count_min = min(self.count_min,level)
        if node.left != None:
            self.min_depth(node.left,level+1)
        if node.right!= None:
            self.min_depth(node.right,level+1)
            
        

sol = Solution()

# input
[]
[1]
[1,2]
[1,2,3]
[1,2,3,4]
[2,null,3,null,4,null,5,null,6]

# output
output = sol.minDepth(root)
# answer
answer = ""
print(output, answer, answer == output)
