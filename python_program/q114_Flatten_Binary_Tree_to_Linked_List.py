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
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return root
        self.flat(root)
        return root

    def flat(self,node):
        if node.left == None and node.right == None:
            return (node,node)
        if node.left != None and node.right == None:
            left_head,left_tail = self.flat(node.left)
            node.left = None
            node.right = left_head
            return (node,left_tail)
        if node.left == None and node.right != None:
            right_head,right_tail = self.flat(node.right)
            node.left = None
            node.right = right_head
            return (node,right_tail)
        if node.left != None and node.right != None:
            left_head,left_tail = self.flat(node.left)
            right_head,right_tail = self.flat(node.right)
            node.left = None
            node.right = left_head
            left_tail.right = right_head
            return (node,right_tail)

sol = Solution()

# input
[1,2,5,3,4,null,6]
[]
[0]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
