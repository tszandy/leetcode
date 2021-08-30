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
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.recursive(root,None)
        hq = [root]
        while hq:
            next_list = []
            for node in hq:
                if node.left!=None:
                    next_list.append(node.left)
                if node.right!=None:
                    next_list.append(node.right)
            if len(next_list)==0:
                break
            hq = next_list
        while not all(map(lambda x:x==hq[0],hq)):
            hq = list(map(lambda x:x.parent,hq))
        return hq[0]
        
    def recursive(self,node,parent):
        if node == None:
            return 
        node.parent = parent
        self.recursive(node.left,node)
        self.recursive(node.right,node)
        

sol = Solution()

# input
[3,5,1,6,2,0,8,null,null,7,4]
[1]
[0,1,3,null,2]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
