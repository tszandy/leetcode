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
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if val >root.val:
            if root.right!=None:
                self.insertIntoBST(root.right,val)
            else:
                root.right = TreeNode(val = val)
        else:
            if root.left!=None:
                self.insertIntoBST(root.left,val)
            else:
                root.left = TreeNode(val = val)
        return root

sol = Solution()

# input
root = [4,2,7,1,3]
val = 5
root = [40,20,60,10,30,50,70]
val = 25
root = [4,2,7,1,3,null,null,null,null,null,null]
val = 5
root = []
val = 5
# output
output = sol.insertIntoBST(root,val)
# answer
answer = ""
print(output, answer, answer == output)
