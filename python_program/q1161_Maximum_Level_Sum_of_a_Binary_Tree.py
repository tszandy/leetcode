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
    def maxLevelSum(self, root: TreeNode) -> int:
        self.max_level_sum = float("-inf")
        self.max_level = 1
        level_list = [root]
        level = 1
        while level_list:
            level_sum = 0
            next_list = []
            for node in level_list:
                level_sum +=node.val
                if node.left!=None:
                    next_list.append(node.left)
                if node.right!=None:
                    next_list.append(node.right)
            if self.max_level_sum < level_sum:
                self.max_level_sum = level_sum
                self.max_level = level
            level_list = next_list
            level+=1
        return self.max_level

sol = Solution()

# input
[1,7,0,7,-8,null,null]
[989,null,10250,98693,-89388,null,null,null,-32127]
[-100,-200,-300,-20,-5,-10,null]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
