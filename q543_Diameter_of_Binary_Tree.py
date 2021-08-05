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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter_list = []
        self.diameter_of_binary_tree(root)
        return max(self.diameter_list)-1
        
    def diameter_of_binary_tree(self,node):
        if node == None:
            return 0
        left_length = self.diameter_of_binary_tree(node.left)
        right_length = self.diameter_of_binary_tree(node.right)
        self.diameter_list.append(1+left_length+right_length)
        return max(left_length,right_length)+1

sol = Solution()

# input
[1,2,3,4,5]
[1,2]

# output
output = sol.diameterOfBinaryTree(root)
# answer
answer = ""
print(output, answer, answer == output)
