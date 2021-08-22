from typing import List
from collections import Counter,defaultdict,deque
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count,zip_longest
import queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.store_list = []
        self.inorder_BST(root)
        n = len(self.store_list)
        return self.construct_BST(0,n-1)
        
    def inorder_BST(self,node):
        if node == None:
            return
        self.inorder_BST(node.left)
        node.left = None
        self.store_list.append(node)
        self.inorder_BST(node.right)
        node.right = None

    def construct_BST(self,l,r):
        if l>r:
            return None
        if l==r:
            return self.store_list[l]
        m = (l+r)//2
        node = self.store_list[m]
        node.left = self.construct_BST(l,m-1)
        node.right = self.construct_BST(m+1,r)
        return node

sol = Solution()

# input
[1,null,2,null,3,null,4]
[2,1,3]

# output
output = sol.balanceBST(root)
# answer
answer = ""
print(output, answer, answer == output)
