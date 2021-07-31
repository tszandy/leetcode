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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.inorder_index_map = {}
        for i,e in enumerate(inorder):
            self.inorder_index_map[e]=i
        n = len(preorder)
        self.preorder = preorder
        self.inorder = inorder
        return self.build_tree(0,n-1,0,n-1)

    def build_tree(self,pre_order_l,pre_order_r,inorder_l,inorder_r):
        if pre_order_l == pre_order_r:
            return TreeNode(val = self.preorder[pre_order_l])
        if pre_order_l>pre_order_r:
            return None
        node = TreeNode(val = self.preorder[pre_order_l])
        node_index = self.inorder_index_map[self.preorder[pre_order_l]]
        left_tree_node = node_index-inorder_l
        node.left = self.build_tree(pre_order_l+1,pre_order_l+left_tree_node,inorder_l,inorder_l+left_tree_node-1)
        node.right = self.build_tree(pre_order_l+left_tree_node+1,pre_order_r,inorder_l+left_tree_node+1,inorder_r)
        return node    

sol = Solution()

# input
[3,9,1,20,15,7]
[1,9,3,15,20,7]
[3,9,1,2,20,15,7]
[1,9,2,3,15,20,7]
[3,9,20,15,7]
[9,3,15,20,7]
[-1]
[-1]
# output
output = sol.buildTree(preorder,inorder)
# answer
answer = ""
print(output, answer, answer == output)
