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
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        return min(self.min_camera_cover(root)[1:])
    
    def min_camera_cover(self,node):
        # three state:
        # state 1: all nodes below current node is covered
        # state 2: all nodes below current node include current node is covered no camera
        # state 3: all nodes below current node is covered, camera in current node
        
        if node == None:
            return 0,0,float('inf')
        L = self.min_camera_cover(node.left)
        R = self.min_camera_cover(node.right)
        
        return_1 = L[1]+R[1]
        return_2 = min(L[2]+min(R[1:]),R[2]+min(L[1:]))
        return_3 = 1 + min(L)+min(R)
        
        return return_1,return_2,return_3


sol = Solution()

# input
[0,0,null,0,0]
[0,0,null,0,null,0,null,null,0]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
