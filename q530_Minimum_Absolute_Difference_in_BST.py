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
    def getMinimumDifference(self, root: TreeNode) -> int:
        BST_list = self.get_minimum_difference(root)
        n = len(BST_list)
        minimum_diff = float("inf")
        for i in range(1,n):
            if abs(BST_list[i]-BST_list[i-1])<minimum_diff:
                minimum_diff = abs(BST_list[i]-BST_list[i-1])
        return minimum_diff

    def get_minimum_difference(self,node):
        if node == None:
            return []
        left = self.get_minimum_difference(node.left)
        right = self.get_minimum_difference(node.right)
        return left + [node.val] + right

sol = Solution()

# input
[4,2,6,1,3]
[1,0,48,null,null,12,49]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
