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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.return_list = []
        self.level_order_bottom(root,0)
        return self.return_list[::-1]
    
    def level_order_bottom(self,node,level):
        if node == None:
            return
        if len(self.return_list)<=level:
            self.return_list.append([])
        self.return_list[level].append(node.val)
        self.level_order_bottom(node.left,level+1)
        self.level_order_bottom(node.right,level+1)

sol = Solution()

# input
[3,9,20,null,null,15,7]
[1]
[]

# output
output = sol.levelOrderBottom(root)
# answer
answer = ""
print(output, answer, answer == output)
