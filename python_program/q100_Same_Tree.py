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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p==None and q == None:
            return True
        if p == None or q == None or p.val !=q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

sol = Solution()

# input
[1,2,3]
[1,2,3]
[1,2]
[1,null,2]
[1,2,1]
[1,1,2]

# output
output = sol.isSameTree(p,q)
# answer
answer = ""
print(output, answer, answer == output)
