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
    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid_BST(root,float("-inf"),float("inf"))
    
    def is_valid_BST(self,node,lower_bound,upper_bound):
        if node == None:
            return True
        return (lower_bound<node.val<upper_bound) and (self.is_valid_BST(node.left,lower_bound,node.val)) and (self.is_valid_BST(node.right,node.val,upper_bound))

sol = Solution()

# input
[2,1,3]
[5,1,4,null,null,3,6]

# output
output = sol.isValidBST(root)
# answer
answer = ""
print(output, answer, answer == output)
