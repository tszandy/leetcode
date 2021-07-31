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
    def goodNodes(self, root: TreeNode) -> int:
        self.count_good_node = 0
        self.good_nodes(root,root.val)
        return self.count_good_node
        
    def good_nodes(self,node,target):
        if node == None:
            return
        if node.val >=target:
            self.count_good_node+=1
        self.good_nodes(node.left,max(target,node.val))
        self.good_nodes(node.right,max(target,node.val))

sol = Solution()

# input
[3,1,4,3,null,1,5]
[3,3,null,4,2]
[1]

# output
output = sol.goodNodes(root)
# answer
answer = ""
print(output, answer, answer == output)
