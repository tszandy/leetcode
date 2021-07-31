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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.return_list = []
        self.inorder_traversal(root)
        return self.return_list
    def inorder_traversal(self,node):
        if node == None:
            return
        self.inorder_traversal(node.left)
        self.return_list.append(node.val)
        self.inorder_traversal(node.right)

sol = Solution()

# input
[1,null,2,3]
[]
[1]
[1,2]
[1,null,2]

# output
output = sol.inorderTraversal(root)
# answer
answer = ""
print(output, answer, answer == output)
