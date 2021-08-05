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
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        self.subRoot = subRoot
        return self.recurrence(root)
        
        
    def recurrence(self,node):
        if node == None:
            return False
        if node.val == self.subRoot.val:
            return self.recurrence(node.left) or self.recurrence(node.right) or self.is_subtree(node,self.subRoot)
        return self.recurrence(node.left) or self.recurrence(node.right)
        
    def is_subtree(self,node,subnode):
        if node == subnode == None:
            return True
        if node == None or subnode == None:
            return False
        if node.val == subnode.val:
            return self.is_subtree(node.left,subnode.left) and self.is_subtree(node.right,subnode.right)
        return False

sol = Solution()

# input
[3,4,5,1,2]
[4,1,2]
[3,4,5,1,2,null,null,null,null,0]
[4,1,2]
[3,4,5,1,null,2]
[3,1,2]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
