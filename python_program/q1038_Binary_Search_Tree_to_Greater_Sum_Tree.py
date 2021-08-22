from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        self.bst_to_gst(root)
        return root
    
    def bst_to_gst(self,node):
        if node ==None:
            return 
        self.bst_to_gst(node.right)
        self.sum+=node.val
        node.val = self.sum
        self.bst_to_gst(node.left)
        

sol = Solution()

# input
root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]

# output
output = sol.bstToGst(root)
# answer
answer = ""
print(output, answer, answer == output)

# input
root = [0,null,1]

# output
output = sol.bstToGst(root)
# answer
answer = ""
print(output, answer, answer == output)

# input
root = [1,0,2]

# output
output = sol.bstToGst(root)
# answer
answer = ""
print(output, answer, answer == output)

# input
root = [3,2,4,1]

# output
output = sol.bstToGst(root)
# answer
answer = ""
print(output, answer, answer == output)
