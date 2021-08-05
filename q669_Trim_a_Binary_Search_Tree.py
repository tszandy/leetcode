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
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        while True:
            if root == None:
                return root
            if low > root.val:
                root = root.right
            if root == None:
                return root
            if root.val > high:
                root = root.left
            if root == None:
                return root
            if low<=root.val<=high:
                break
        root.left = self.trimBST(root.left,low,high)
        root.right = self.trimBST(root.right,low,high)
        return root

sol = Solution()

# input
[1,0,2]
1
2
[3,0,4,null,2,null,null,1]
1
3
[1]
1
2
[1,null,2]
1
3
[1,null,2]
2
4

# output
output = sol.trimBST(root,low,high)
# answer
answer = ""
print(output, answer, answer == output)
