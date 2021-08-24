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
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deep_leave_sum = 0
        node_list = [root]
        while node_list:
            next_list = []
            level_sum = 0
            for node in node_list:
                level_sum+=node.val
                if node.left!=None:
                    next_list.append(node.left)
                if node.right!=None:
                    next_list.append(node.right)
            deep_leave_sum = level_sum
            node_list = next_list
        return deep_leave_sum

sol = Solution()

# input
[1,2,3,4,5,null,6,7,null,null,null,null,8]

[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]

# output
output = sol.deepestLeavesSum(root)
# answer
answer = ""
print(output, answer, answer == output)
