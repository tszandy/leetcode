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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.sum_root_to_leaf(root,"")
        return self.sum 

    def sum_root_to_leaf(self,node,string):
        if node == None:
            return
        next_string = string+str(node.val)
        if node.left==node.right==None:
            self.sum += int(next_string,2)
        else:
            self.sum_root_to_leaf(node.left,next_string)
            self.sum_root_to_leaf(node.right,next_string)

sol = Solution()

# input
[1,0,1,0,1,0,1]
[0]
[1]
[1,1]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
