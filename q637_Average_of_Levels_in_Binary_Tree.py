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
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        self.level_sum = []
        self.level_count = []
        self.average_of_levels(root,0)
        return list(map(lambda x:x[0]/x[1],zip(self.level_sum,self.level_count)))

    def average_of_levels(self,node,level):
        if node == None:
            return
        if len(self.level_sum)<=level:
            self.level_sum.append(node.val)
            self.level_count.append(1)
        else:
            self.level_sum[level]+=node.val
            self.level_count[level]+=1
        self.average_of_levels(node.left,level+1)
        self.average_of_levels(node.right,level+1)


sol = Solution()

# input
[3,9,20,null,null,15,7]
[3,9,20,15,7]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
