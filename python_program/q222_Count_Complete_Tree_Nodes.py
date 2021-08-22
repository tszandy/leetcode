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
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.count = 0
        self.count_node(root)
        return self.count

    def count_node(self,node):
        self.count+=1
        if node.left!=None:
            self.count_node(node.left)
            if node.right != None:
                self.count_node(node.right)
        

sol = Solution()

# input
[1,2,3,4,5,6]
[]
[1]

# output
output = sol.countNodes(root)
# answer
answer = ""
print(output, answer, answer == output)
