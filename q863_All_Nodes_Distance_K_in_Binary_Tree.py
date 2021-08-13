from typing import List
from collections import Counter,defaultdict,deque
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count
import queue

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        self.recursive(root)

        q = []
        q.append((target,0))
        
        visited_set = set([target])

        while q:
            if q[0][1]==k:
                return [node.val for node,d in q]
            node, d = q.pop(0)
            for nei in (node.left,node.right,node.par):
                if nei and nei not in visited_set:
                    visited_set.add(nei)
                    q.append((nei,d+1))
        return []


    def recursive(self,node,par = None):
        if node:
            node.par = par
            self.recursive(node.left,node)
            self.recursive(node.right,node)

sol = Solution()

# input
[3,5,1,6,2,0,8,null,null,7,4]
5
2
[1]
1
3

# output
output = sol.distanceK(root,target,k)
# answer
answer = ""
print(output, answer, answer == output)
