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
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.to_delete = set(to_delete+[None])
        self.store_result = []
        root = TreeNode(val = None,left = root)
        hq= [root]
        while hq:
            node = hq.pop(0)
            if node.left!=None:
                hq.append(node.left)
            if node.right!=None:
                hq.append(node.right)
            if node.val in self.to_delete:
                if node.left!=None:
                    if node.left.val not in self.to_delete:
                        self.store_result.append(node.left)
                if node.right!=None: 
                    if node.right.val not in self.to_delete:
                        self.store_result.append(node.right)
            if node.left!=None and node.left.val in self.to_delete:
                node.left = None
            if node.right!=None and node.right.val in self.to_delete:
                node.right = None
        return self.store_result

sol = Solution()

# input
[1,2,3,4,5,6,7]
[3,5]
[1,2,4,null,3]
[3]
[1,2,4,null,3]
[]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
