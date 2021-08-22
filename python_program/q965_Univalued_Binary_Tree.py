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
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return self.is_unival_tree(root.left,root.val) and self.is_unival_tree(root.right,root.val)
    
    def is_unival_tree(self,node,val):
        if node == None:
            return True
        if node.val != val:
            return False
        else:
            return self.is_unival_tree(node.left,val) and self.is_unival_tree(node.right,val)

sol = Solution()

# input
[1,1,1,1,1,null,1]
[2,2,2,5,2]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
