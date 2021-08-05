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
    def tree2str(self, root: TreeNode) -> str:
        return self.tree_2_str(root)

    def tree_2_str(self,node):
        if node == None:
            return ""
        return_str = str(node.val)
        if node.left==node.right==None:
            return_str+=""
        else:
            return_str+="("+self.tree_2_str(node.left)+")"
            if node.right!=None:
                return_str+="("+self.tree_2_str(node.right)+")"
        return return_str

sol = Solution()

# input
[1,2,3,4]
[1,2,3,null,4]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
