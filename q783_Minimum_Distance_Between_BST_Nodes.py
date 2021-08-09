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
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        return self.min_difference(root)
        
    def min_difference(self,node):
        if node == None:
            return float("inf")

        node_left_min = float("inf")
        if node.left!=None:
            node_left_min = node.val-self.max_left(node.left)

        node_right_min = float("inf")
        if node.right!=None:
            node_right_min = self.max_right(node.right)-node.val
       
        left_min = self.min_difference(node.left)
        
        right_min = self.min_difference(node.right)
        
        return min(node_left_min,node_right_min,left_min,right_min)

    def max_left(self,node):
        if node.right == None:
            return node.val
        else:
            return self.max_left(node.right)

    def max_right(self,node):
        if node.left == None:
            return node.val
        else:
            return self.max_right(node.left)

sol = Solution()

# input
[4,2,6,1,3]
[1,0,48,null,null,12,49]
[1,0]
[2,0,5]
[2,0,6]
[5,0,13]

# output
output = sol.minDiffInBST(root)
# answer
answer = ""
print(output, answer, answer == output)
