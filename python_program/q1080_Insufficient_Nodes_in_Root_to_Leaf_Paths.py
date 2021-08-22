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
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        self.limit = limit
        self.insufficient(root,0)
        return root
        
    def insufficient(self,node,val):
        if node == None:
            return True
        left = self.insufficient(node.left,val+node.val)
        right = self.insufficient(node.right,val+node.val)

        if node.left == node.right == None:
            return_val = val+node.val<self.limit
        else:
            return_val = left and right

        if left:
            node.left = None
        if right:
            node.right = None
        return return_val

sol = Solution()

# input
[1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14]
1
[5,4,8,11,null,17,4,7,1,null,null,5,3]
22
[1,2,-3,-5,null,4,null]
-1
[10,5,10]
21

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
