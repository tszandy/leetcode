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
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

sol = Solution()

# input
[3,9,20,null,null,15,7]
[1,null,2]
[]
[0]
# output
output = sol.maxDepth(root)
# answer
answer = ""
print(output, answer, answer == output)
