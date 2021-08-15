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
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.max_difference = 0
        self.min_max(root,0)
        return self.max_difference
        
    def min_max(self,node,val):
        if node == None:
            return val,val
        left = self.min_max(node.left,node.val)
        right = self.min_max(node.right,node.val)
        min_num = min(left[0],right[0],node.val)
        max_num = max(left[1],right[1],node.val)
        self.max_difference = max(abs(node.val-min_num),abs(node.val-max_num),self.max_difference)
        return min_num,max_num

sol = Solution()

# input
[8,3,10,1,6,null,14,null,null,4,7,13]
[1,null,2,null,0,3]
[7,5,12,11,0,2,null,4,17,6,19,null,16,18,null,null,null,null,9,14,10,null,null,null,null,null,null,null,null,3,1,null,null,8,null,13,null,null,15]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
