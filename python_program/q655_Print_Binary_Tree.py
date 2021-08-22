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
    def printTree(self, root: TreeNode) -> List[List[str]]:
        self.max_level = 0
        self.get_max_level(root,1)
        m = self.max_level
        n = 2**(self.max_level)-1
        self.return_list = [[""]*n for _ in range(m)]
        self.print_tree(0,n-1,0,root)
        return self.return_list

    def get_max_level(self,node,level):
        if node == None:
            return
        self.max_level = max(level,self.max_level)
        self.get_max_level(node.left,level+1)
        self.get_max_level(node.right,level+1)
    
    def print_tree(self,l,r,level,node):
        if node == None:
            return
        if level<self.max_level:
            m = (l+r)//2
            self.return_list[level][m] = str(node.val)
            self.print_tree(l,m-1,level+1,node.left)
            self.print_tree(m+1,r,level+1,node.right)

sol = Solution()

# input
[1]
[1,2]
[1,2,3,null,4]
[10,5,15,null,null,6,20]
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
