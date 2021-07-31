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
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.return_list = []
        self.right_side_view(root,0)
        return self.return_list
        
    def right_side_view(self,node,level):
        if node == None:
            return
        if len(self.return_list)<=level:
            self.return_list.append(node.val)
        if node.right != None:
            self.right_side_view(node.right,level+1)
        if node.left != None:
            self.right_side_view(node.left,level+1)

sol = Solution()

# input
[1,2,3,null,null,4,5,6,null,null,null,7,null,8,null]
[1,2,3,null,null,4,null,null,5]
[1,null,3,1,null]
[1,2,3,null,5,null,4]
[1,null,3]
[]
# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
