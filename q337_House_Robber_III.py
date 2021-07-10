from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
from bisect import bisect_left

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        rob_without_node = {}
        rob_with_node = {}
        
        def rob_value_without(node):
            if node in rob_without_node:
                return rob_without_node[node]
            
            amount = []
            if node.left:
                left_node_without_partent_node = rob_value_without(node.left)
                left_node_with_partent_node = rob_value_with(node.left)
                amount.append(max(left_node_without_partent_node,left_node_with_partent_node))
            if node.right:
                right_node_without_partent_node = rob_value_without(node.right)
                right_node_with_partent_node = rob_value_with(node.right)
                amount.append(max(right_node_without_partent_node,right_node_with_partent_node))
            
            rob_without_node[node] = sum(amount)
            
            return rob_without_node[node]
        
        def rob_value_with(node):
            if node in rob_with_node:
                return rob_with_node[node]
            
            amount = []
            if node.left:
                left_node_without_partent_node = rob_value_without(node.left)
                amount.append(left_node_without_partent_node)
            if node.right:
                right_node_without_partent_node = rob_value_without(node.right)
                amount.append(right_node_without_partent_node)
            rob_with_node[node] = sum(amount)+node.val
            
            return rob_with_node[node]
        rob_without_root = rob_value_without(root)
        rob_with_root = rob_value_with(root)
        
        return max(rob_without_root,rob_with_root)
            

sol = Solution()


# input
TreeNode = [3,2,3,null,3,null,1]

# output
output = sol.rob(TreeNode)
# answer
answer = ""
print(output, answer, answer == output)

# input
TreeNode = [3,2,3,null,3,null,1]

# output
output = sol.rob(TreeNode)
# answer
answer = ""
print(output, answer, answer == output)

# input
TreeNode = [3,2,3,3,3,2,11,2,3,4,1,2,1,1,2,3,11,5,1,2,4,3,2,5,7,1,2,null,2]

# output
output = sol.rob(TreeNode)
# answer
answer = ""
print(output, answer, answer == output)
