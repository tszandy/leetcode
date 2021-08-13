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
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if root == None:
            return 0
        if low<=root.val <=high:
            return self.rangeSumBST(root.left,low,high) + root.val + self.rangeSumBST(root.right,low,high)
        elif root.val <low:
            return self.rangeSumBST(root.right,low,high)
        elif root.val > high:
            return self.rangeSumBST(root.left,low,high)

sol = Solution()

# input
[10,5,15,3,7,null,18]
7
15
[10,5,15,3,7,13,18,1,null,6]
6
10

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
