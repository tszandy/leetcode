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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return root
        self.return_list = []
        self.postorder_traversal(root)
        return self.return_list
        
    def postorder_traversal(self,node):
        if node.left != None:
            self.postorder_traversal(node.left)
        if node.right != None:
            self.postorder_traversal(node.right)
        self.return_list.append(node.val)


sol = Solution()

# input
[9,1,2,null,3,4,1,2,null,1,3,null]
[1,null,2,3]
[]
[1]
[1,2]
[1,null,2]

# output
output = sol.postorderTraversal(root)
# answer
answer = ""
print(output, answer, answer == output)
