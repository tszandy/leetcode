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
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.visited_num = set()
        self.k = k
        return self.find_target(root)

    def find_target(self,node):
        if node == None:
            return False
        if self.k-node.val in self.visited_num:
            return True
        self.visited_num.add(node.val)
        return self.find_target(node.left) or self.find_target(node.right)

sol = Solution()

# input
[5,3,6,2,4,null,7]
9
[5,3,6,2,4,null,7]
28
[2,1,3]
4
[2,1,3]
1
[2,1,3]
3

# output
output = sol.findTarget(root)
# answer
answer = ""
print(output, answer, answer == output)
