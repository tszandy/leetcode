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
    def maxPathSum(self, root: TreeNode) -> int:
        self.store_double_max = {}
        self.max_path_sum(root)
        return max(self.store_double_max.values())
    def max_path_sum(self,node):
        if node == None:
            return 0 
        left = self.max_path_sum(node.left)
        right = self.max_path_sum(node.right)
        self.store_double_max[node] = left+right+node.val
        single_sum = max(left,right)+node.val
        if single_sum >0:
            return single_sum
        else:
            return 0        

sol = Solution()

# input
[1,2,3]
[-10,9,20,null,null,15,7]

# output
output = sol.maxPathSum(root)
# answer
answer = ""
print(output, answer, answer == output)
