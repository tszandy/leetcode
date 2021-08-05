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
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.first_min = float("inf")
        self.second_min = float("inf")
        self.find_second_min_val(root)
        if self.second_min == float("inf"):
            return -1
        else:
            return self.second_min
        
    def find_second_min_val(self,node):
        if node == None:
            return
        if not(node.val == self.first_min or node.val == self.second_min): 
            if node.val<self.first_min:
                self.second_min = self.first_min
                self.first_min = node.val
            elif node.val<self.second_min:
                self.second_min = node.val
        self.find_second_min_val(node.left)
        self.find_second_min_val(node.right)

sol = Solution()

# input
[2,2,5,null,null,5,7]
[1,1,2,1,3,2,5]
[2,2,2]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
