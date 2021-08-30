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
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        self.x = x
        self.n = n
        self.return_result = False
        self.recursive(root)
        return self.return_result

    def recursive(self,node):
        if node ==None:
            return False
        if node.val == self.x:
            count_left = self.count(node.left)
            count_right = self.count(node.right)
            count_up = self.n-count_left-count_right-1
            if count_left>self.n//2 or count_right>self.n//2 or count_up>self.n//2:
                self.return_result=True
                return
        self.recursive(node.left)
        self.recursive(node.right)
        
            
    def count(self,node):
        if node == None:
            return 0
        return self.count(node.left)+self.count(node.right)+1

sol = Solution()

# input
[1,2,3,4,5,6,7,8,9,10,11]
11
3
[1,2,3]
3
1

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
