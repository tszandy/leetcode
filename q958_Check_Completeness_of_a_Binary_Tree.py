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
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        last_row = False
        last_node = False
        level_list = [root]
        while level_list:
            next_list = []
            for node in level_list:
                if node != None:
                    if not last_node:
                        next_list.append(node.left)
                        next_list.append(node.right)
                    else:
                        return False
                else:
                    last_node = True
            level_list = next_list
        return True


sol = Solution()

# input
[1]
[1,2,3,4,5,6]
[1,2,3,4,5,null,7]
[1,2,3,null,5,6,7]
[1,2,3,4,5,6,7,8]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
