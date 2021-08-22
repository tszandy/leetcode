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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.level_order_dict = defaultdict(list)
        self.level_order(root,0)
        return_list = []
        for key in sorted(self.level_order_dict.keys()):
            return_list.append(self.level_order_dict[key])
        return return_list

    def level_order(self,node, level):
        if node == None:
            return
        self.level_order_dict[level].append(node.val)
        self.level_order(node.left,level+1)
        self.level_order(node.right,level+1)

sol = Solution()

# input
[3,9,20,null,null,15,7]
[1]
[]

# output
output = sol.levelOrder(root)
# answer
answer = ""
print(output, answer, answer == output)
