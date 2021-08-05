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
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.longest = float("-inf")
        self.longest_univalue_path(root)
        return self.longest-1

        
    def longest_univalue_path(self,node):
        left = 0
        if node.left!=None: 
            left_path_length = self.longest_univalue_path(node.left)
            if node.left.val == node.val:
                left = left_path_length
        right = 0
        if node.right!=None:
            right_path_length = self.longest_univalue_path(node.right)
            if node.right.val == node.val:
                right = right_path_length
        self.longest = max(left+right+1,self.longest)
        return max(left,right)+1

sol = Solution()

# input
[5,4,5,1,1,5]
[1,4,5,4,4,5]

# output
output = sol.longestUnivaluePath(root)
# answer
answer = ""
print(output, answer, answer == output)
