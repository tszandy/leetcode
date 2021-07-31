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
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_symmetric(root.left,root.right)
        
    def is_symmetric(self,node_1,node_2):
        if node_1 == None and node_2 == None:
            return True
        elif node_1 != None and node_2 != None:        
            return node_1.val == node_2.val and self.is_symmetric(node_1.right,node_2.left)and self.is_symmetric(node_1.left,node_2.right)
        else:
            return False

sol = Solution()

# input
[1,2,2,3,4,4,3]
[1,2,2,null,3,null,3]

# output
output = sol.isSymmetric(root)
# answer
answer = ""
print(output, answer, answer == output)
