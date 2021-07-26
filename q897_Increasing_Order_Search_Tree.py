from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.root = None
        self.increasing_BST(root)
        return self.root
        
    def increasing_BST(self,node):
        if node==None:
            return
        self.increasing_BST(node.left)
        if self.root==None:
            self.root = TreeNode(val = node.val)
            self.track = self.root
        else:
            self.track.right = TreeNode(val = node.val)
            self.track = self.track.right
        self.increasing_BST(node.right)
        

sol = Solution()

# input
root = [5,3,6,2,4,null,8,1,null,null,null,7,9]

# output
output = sol.increasingBST(root)
# answer
answer = ""
print(output, answer, answer == output)

# input
root = [5,1,7]

# output
output = sol.increasingBST(root)
# answer
answer = ""
print(output, answer, answer == output)
