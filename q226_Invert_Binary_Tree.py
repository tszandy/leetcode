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
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.invert_tree(root)
        return root        
        
    def invert_tree(self,node):
        if node == None:
            return
        node.right,node.left = node.left,node.right
        self.invert_tree(node.left)
        self.invert_tree(node.right)

sol = Solution()

# input
[4,2,7,1,3,6,9]
[4,2,7,1,3,6]
[2,1,3]
[]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
