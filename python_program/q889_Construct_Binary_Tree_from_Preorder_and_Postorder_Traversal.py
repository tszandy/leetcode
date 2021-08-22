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
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.postorder = postorder
        self.pre_order_map = {}
        self.post_order_map = {}
        n = len(preorder)
        for i in range(n):
            self.pre_order_map[preorder[i]]=i
            self.post_order_map[postorder[i]]=i
        return self.construct_from_pre_post(0,n-1,0,n-1)

    def construct_from_pre_post(self,pre_l,pre_r,post_l,post_r):
        if pre_l>pre_r:
            return None
        if pre_l == pre_r:
            return TreeNode(self.preorder[pre_l])
        left_tree_head = self.preorder[pre_l+1]
        right_tree_head = self.postorder[post_r-1]
        left = self.construct_from_pre_post(pre_l+1,self.pre_order_map[right_tree_head]-1,post_l,self.post_order_map[left_tree_head])
        right = self.construct_from_pre_post(self.pre_order_map[right_tree_head],pre_r,self.post_order_map[left_tree_head]+1,post_r-1)        
        return TreeNode(val = self.preorder[pre_l],left = left,right=right)

sol = Solution()

# input
[1,2,4,5,3,6,7]
[4,5,2,6,7,3,1]
[1]
[1]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
