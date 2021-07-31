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
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.list_iterator = iter(preorder)
        elem = next(self.list_iterator,None)
        root = TreeNode(val = elem)
        for elem in self.list_iterator:
            self.bst_from_preorder(root,elem)
        return root
        
    def bst_from_preorder(self,node,target):
        if target >node.val:
            if node.right == None:
                node.right = TreeNode(target)
            else:
                self.bst_from_preorder(node.right,target)
        if target < node.val:
            if node.left == None:
                node.left = TreeNode(target)
            else:
                self.bst_from_preorder(node.left,target)

sol = Solution()

# input
[8,5,1,7,10,12]
[1,3]
[1]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
