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
    def findMode(self, root: TreeNode) -> List[int]:
        self.counter = Counter()
        self.recurence(root)
        max_count = max(self.counter.values())
        return [key for key,val in self.counter.items() if val == max_count]
        
    def recurence(self,node):
        if node == None:
            return 
        self.counter[node.val]+=1
        self.recurence(node.left)
        self.recurence(node.right)

sol = Solution()

# input
[2,1,2,1]
[1,null,2,2]
[0]
# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
