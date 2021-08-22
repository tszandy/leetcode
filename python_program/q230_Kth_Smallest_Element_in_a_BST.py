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
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.min_elem = None
        self.kth_smallest(root,k)
        return self.min_elem

    def kth_smallest(self,node,k):
        if node == None:
            return 0

        left = self.kth_smallest(node.left,k)
        if left+1==k:
            self.min_elem = node.val
        right = self.kth_smallest(node.right,k-left-1)
        return left + right + 1

sol = Solution()

# input
[3,1,4,null,2]
1
[5,3,6,2,4,null,null,1]
3
# output
output = sol.kthSmallest(root,k)
# answer
answer = ""
print(output, answer, answer == output)
