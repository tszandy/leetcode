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
    def findTilt(self, root: TreeNode) -> int:
        self.absolute_difference_sum = 0
        self.find_tilt(root)
        return self.absolute_difference_sum

    def find_tilt(self,node):
        if node == None:
            return 0 
        left = self.find_tilt(node.left)
        right = self.find_tilt(node.right)
        self.absolute_difference_sum+=abs(left-right)
        return left+right+node.val

sol = Solution()

# input
[1,2,3]
[4,2,9,3,5,null,7]
[21,7,14,1,1,2,2,3,3]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
