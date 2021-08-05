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
    def largestValues(self, root: TreeNode) -> List[int]:
        self.return_list = []
        self.largest_values(root,0)
        return self.return_list
        
        
    def largest_values(self,node,level):
        if node == None:
            return
        if len(self.return_list)<=level:
            self.return_list.append(node.val)
        if self.return_list[level]<node.val:
            self.return_list[level] = node.val
        self.largest_values(node.left,level+1)
        self.largest_values(node.right,level+1)

sol = Solution()

# input
[1,3,2,5,3,null,9]
[1,2,3]
[1]
[1,null,2]
[]

# output
output = sol.largestValues(root)
# answer
answer = ""
print(output, answer, answer == output)
