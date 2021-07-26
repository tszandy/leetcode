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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.get_target_copy(cloned,target)
        
        
        
        
    def get_target_copy(self,node,target):
        if node == None:
            return None
        if self.compare_two_node(node,target):
            return node
        left = self.get_target_copy(node.left,target)
        right = self.get_target_copy(node.right,target)
        if left:
            return left
        if right:
            return right
        
        
    def compare_two_node(self,node_1,node_2):
        if node_1 and node_2 and node_1.val == node_2.val:
            cond_1 = self.compare_two_node(node_1.left,node_2.left)
            cond_2 = self.compare_two_node(node_1.right,node_2.right)
            return cond_1 and cond_2
        elif not node_1 and not node_2:
            return True
        else:
            return False

sol = Solution()

# input
tree = [7,4,3,null,null,6,19]

target = 3

# output
output = sol.getTargetCopy(original,cloned,target)
# answer
answer = ""
print(output, answer, answer == output)

# input
tree = [7]

target = 7

# output
output = sol.getTargetCopy(original,cloned,target)
# answer
answer = ""
print(output, answer, answer == output)

# input
tree = [8,null,6,null,5,null,4,null,3,null,2,null,1]

target = 4

# output
output = sol.getTargetCopy(original,cloned,target)
# answer
answer = ""
print(output, answer, answer == output)

# input
tree = [1,2,3,4,5,6,7,8,9,10]

target = 5

# output
output = sol.getTargetCopy(original,cloned,target)
# answer
answer = ""
print(output, answer, answer == output)

# input
tree = [1,2,null,3]

target = 2

# output
output = sol.getTargetCopy(original,cloned,target)
# answer
answer = ""
print(output, answer, answer == output)
