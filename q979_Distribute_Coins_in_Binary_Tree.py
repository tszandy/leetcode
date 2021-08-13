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
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        self.distribute_coins(root)
        return self.moves

    def distribute_coins(self,node):
        if node == None:
            return 0 
        l_excess,r_excess = self.distribute_coins(node.left),self.distribute_coins(node.right)
        self.moves += abs(l_excess)+abs(r_excess)
        return node.val + l_excess+r_excess-1



sol = Solution()

# input
[3,0,0]
[0,3,0]
[1,0,2]
[1,0,0,null,3]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
