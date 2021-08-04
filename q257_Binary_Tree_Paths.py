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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root == None:
            return []
        self.return_list = []
        self.binary_tree_paths(root,[])
        return self.return_list
        
        
    def binary_tree_paths(self,node,store_list):
        if node.left==node.right==None:
            self.return_list.append("->".join(store_list+[str(node.val)]))
            return 
        if node.left != None:
            self.binary_tree_paths(node.left,store_list+[str(node.val)])
        if node.right != None:
            self.binary_tree_paths(node.right,store_list+[str(node.val)])

sol = Solution()

# input
[1,2,3,null,5]
[1]

# output
output = sol.binaryTreePaths(root)
# answer
answer = ""
print(output, answer, answer == output)
