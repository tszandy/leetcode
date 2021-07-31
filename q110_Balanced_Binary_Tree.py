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
    def isBalanced(self, root: TreeNode) -> bool:
        if self.is_balanced(root)==-1:
            return False
        return True

    def is_balanced(self,node):
        if node == None:
            return 0
        left_level = self.is_balanced(node.left)
        right_level = self.is_balanced(node.right)
        if left_level == -1 or right_level == -1:
            return -1
        if abs(left_level-right_level)>=2:
            return -1
        else:
            return max(left_level,right_level)+1
        

sol = Solution()

# input
[3,9,20,null,null,15,7]
[1,2,2,3,3,null,null,4,4]
[]

# output
output = sol.isBalanced(root)
# answer
answer = ""
print(output, answer, answer == output)
