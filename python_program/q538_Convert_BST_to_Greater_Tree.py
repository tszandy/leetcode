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
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.count = 0
        if root == None:
            return None
        self.convert_BST(root)
        return root
        
        
    def convert_BST(self,node):
        if node == None:
            return
        self.convert_BST(node.right)
        self.count+=node.val
        node.val = self.count
        self.convert_BST(node.left)

sol = Solution()

# input
[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
[0,null,1]
[1,0,2]
[3,2,4,1]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
