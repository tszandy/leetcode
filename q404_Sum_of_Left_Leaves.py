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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0
        self.recursive(root)
        return self.sum

    def recursive(self,node):
        if node == None:
            return
        if node.left!=None:
            if node.left.left == None and node.left.right == None:
                self.sum+=node.left.val
            self.recursive(node.left)
        if node.right!=None:
            self.recursive(node.right)
        

sol = Solution()

# input
[3,9,20,null,null,15,7]
[1]

# output
output = sol.sumOfLeftLeaves(root)
# answer
answer = ""
print(output, answer, answer == output)
