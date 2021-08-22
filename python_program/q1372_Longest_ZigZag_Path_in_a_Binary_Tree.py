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
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest_zig_zag = 0
        self.zigzag(root)
        return self.longest_zig_zag-1
        
    def zigzag(self,node):
        if node == None:
            return 0,0
        left = self.zigzag(node.left)
        right = self.zigzag(node.right)
        return_l = left[1]+1
        return_r = right[0]+1
        self.longest_zig_zag = max(self.longest_zig_zag,return_l,return_r)
        return (return_l,return_r)


sol = Solution()

# input
[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
[1,1,1,null,1,null,null,1,1,null,1]
[1]

# output
output = sol.longestZigZag(root)
# answer
answer = ""
print(output, answer, answer == output)
