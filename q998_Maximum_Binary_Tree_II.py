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
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if val >root.val:
            return TreeNode(val = val,left = root)
        self.insert_into_max_tree(root.right,val,par = root)
        return root
    
    def insert_into_max_tree(self,node,val,par=None):
        if node == None:
            par.right = TreeNode(val=val)
            return 
        if node.val<val:
            par.right = TreeNode(val = val,left = node)
        else:
            self.insert_into_max_tree(node.right,val,node)
        

sol = Solution()

# input
[4,1,3,null,null,2]
5
[5,2,4,null,1]
3
[5,2,3,null,1]
4

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
