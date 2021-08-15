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
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.distance = distance
        self.count = 0
        self.count_pair(root)
        return self.count
    
    def count_pair(self,node):
        if node == None:
            return []
        left = self.count_pair(node.left)
        right = self.count_pair(node.right)
        
        if len(left)!=0 and len(right)!=0:
            for i in left:
                for j in right:
                    if i + j<=self.distance:
                        self.count+=1
        return_list = []
        if len(left)!=0:
            for i in left:
                return_list.append(i+1)
        if len(right)!=0:
            for i in right:
                return_list.append(i+1)
        if len(return_list)==0:
            return_list.append(1)
        return return_list

sol = Solution()

# input
[1,2,3,null,4]
3
[1,2,3,4,5,6,7]
3
[7,1,4,6,null,5,3,null,null,null,null,null,2]
3
[100]
1
[1,1,1]
2

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
