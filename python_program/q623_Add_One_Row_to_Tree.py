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
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        root = TreeNode(val = None,left = root)
        self.val = val
        self.depth = depth
        self.add_one_row(root,0)
        return root.left
    
    def add_one_row(self,node,level):
        if node == None:
            return
        if level+1 == self.depth:
            node.left = TreeNode(val = self.val,left=node.left)
            node.right = TreeNode(val = self.val,right=node.right)
        else:
            self.add_one_row(node.left,level+1)
            self.add_one_row(node.right,level+1)

sol = Solution()

# input
[4,2,6,3,1,5]
1
2
[4,2,null,3,1]
1
3
[4,2,null,3,1]
1
4
[1]
1
2

# output
output = sol.addOneRow(root,val,depth)
# answer
answer = ""
print(output, answer, answer == output)
