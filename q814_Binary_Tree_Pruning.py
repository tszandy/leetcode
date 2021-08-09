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
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        if not self.prune_tree(root):
            return None
        else:
            return root
        
        
    def prune_tree(self,node):
        if node == None:
            return False
        left = self.prune_tree(node.left)
        if not left:
            node.left = None
        right = self.prune_tree(node.right)
        if not right:
            node.right = None
        return left or right or node.val == 1

sol = Solution()

# input
[1,null,0,0,1]
[1,0,1,0,0,0,1]
[1,1,0,1,1,0,1,0]
[0]
[1]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
