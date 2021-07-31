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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return root
        self.return_list = []
        self.preorder_traversal(root)
        return self.return_list

    def preorder_traversal(self,node):
        if node == None:
            return
        self.return_list.append(node.val)
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)

sol = Solution()

# input
[9,1,2,null,3,4,1,2,null,1,3,null]
[1,null,2,3]
[]
[1]
[1,2]
[1,null,2]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
