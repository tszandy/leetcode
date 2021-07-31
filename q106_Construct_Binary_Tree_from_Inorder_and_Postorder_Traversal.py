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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.inorder = inorder
        self.postorder = postorder
        self.inorder_num_to_index = {}
        for i,e in enumerate(inorder):
            self.inorder_num_to_index[e]=i
        n = len(inorder)
        return self.build_tree(0,n-1,0,n-1)
        
    def build_tree(self,inorder_l,inorder_r,postorder_l,postorder_r):
        if inorder_l == inorder_r:
            return TreeNode(val = self.inorder[inorder_l])
        if inorder_l>inorder_r:
            return None
        node = TreeNode(val = self.postorder[postorder_r])
        node_inorder_index = self.inorder_num_to_index[node.val]
        right_tree_length = inorder_r - node_inorder_index
        left_tree_length = node_inorder_index - inorder_l
        node.left = self.build_tree(inorder_l,inorder_l+left_tree_length-1,postorder_l,postorder_l+left_tree_length-1)
        node.right = self.build_tree(inorder_r-right_tree_length+1,inorder_r,postorder_r-right_tree_length,postorder_r-1)
        return node

sol = Solution()

# input
[9,3,15,20,7]
[9,15,7,20,3]
[-1]
[-1]
# output
output = sol.buildTree(inorder,postorder)
# answer
answer = ""
print(output, answer, answer == output)
