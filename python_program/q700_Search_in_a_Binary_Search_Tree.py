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
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left,val)
        if root.val < val:
            return self.searchBST(root.right,val)

sol = Solution()

# input
[4,2,7,1,3]
2
[4,2,7,1,3]
5

# output
output = sol.searchBST(root,val)
# answer
answer = ""
print(output, answer, answer == output)
