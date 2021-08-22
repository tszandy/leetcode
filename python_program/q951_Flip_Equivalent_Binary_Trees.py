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
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if ((root1==None) ^ (root2==None)):
            return False
        elif root1 == None and root2 == None:
            return True
        else:
            if root1.val !=root2.val:
                return False
            else:
                return (self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right)) or (self.flipEquiv(root1.left,root2.right) and self.flipEquiv(root1.right,root2.left))

sol = Solution()

# input
[1,2,3,4,5,6,null,null,null,7,8]
[1,3,2,null,6,4,5,null,null,null,null,8,7]
[]
[]
[]
[1]
[0,null,1]
[]
[0,null,1]
[0,1]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
