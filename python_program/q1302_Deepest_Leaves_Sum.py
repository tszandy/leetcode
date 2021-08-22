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
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.max_depth = 0
        self.store_list = []
        self.get_deepest_leave(0,root)
        return sum(self.store_list)        
    def get_deepest_leave(self,depth,node):
        if node == None:
            return
        else:
            if depth >self.max_depth:
                self.max_depth = depth
                self.store_list = []            
                self.store_list.append(node.val)
            elif depth == self.max_depth:
                self.store_list.append(node.val)
            self.get_deepest_leave(depth+1,node.left)
            self.get_deepest_leave(depth+1,node.right)

sol = Solution()

# input
root = [1,2,3,4,5,null,6,7,null,null,null,null,8]

# output
output = sol.deepestLeavesSum(root)
# answer
answer = ""
print(output, answer, answer == output)

# input
root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]

# output
output = sol.deepestLeavesSum(root)
# answer
answer = ""
print(output, answer, answer == output)
