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
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.index = 0
        self.voyage = voyage
        self.swap = []
        if self.flip_match(root):
            return self.swap
        else:
            return [-1]

    def flip_match(self,node):
        if node.val != self.voyage[self.index]:
            return False
        self.index+=1
        if node.left==None and node.right!=None:
            node.left,node.right = node.right,node.left
            if not self.flip_match(node.left):
                return False
        elif node.left!=None and node.right!=None:
            if node.left.val !=self.voyage[self.index]:
                node.left,node.right = node.right,node.left
                self.swap.append(node.val)
            if not(self.flip_match(node.left) and self.flip_match(node.right)):
                return False
        elif node.left!=None and node.right==None:
            if not(self.flip_match(node.left)):
                return False
        return True

sol = Solution()

# input
[1,2]
[2,1]
[1,2,3]
[1,3,2]
[1,2,3]
[1,2,3]
[1,3,2,4,5]
[1,2,3,4,5]
[1,3,2,7,6,5,4]
[1,2,4,5,3,6,7]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
