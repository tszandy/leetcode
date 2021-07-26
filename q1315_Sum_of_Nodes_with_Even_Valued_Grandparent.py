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
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum=[0]
        self.recursive_tree(root)
        return sum(self.sum)
    
    def recursive_tree(self,node):
        if node == None:
            return
        if node.val%2==0:
            self.add_all_grandchild(node)
        self.recursive_tree(node.left)
        self.recursive_tree(node.right)
        
        
    def add_all_grandchild(self,node):
        self.add_all_child(node.left)
        self.add_all_child(node.right)        
    
    def add_all_child(self,node):
        if node == None:
            return
        self.add_node(node.left)
        self.add_node(node.right)
        
    def add_node(self,node):
        if node == None:
            return
        self.sum.append(node.val)

sol = Solution()

# input
root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]

# output
output = sol.sumEvenGrandparent(root)
# answer
answer = ""
print(output, answer, answer == output)
