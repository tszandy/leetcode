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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.parent_list = []
        self.p = p
        self.q = q
        self.get_parent_list(root,[])
        l,r = self.parent_list
        n = min(len(l),len(r))
        min_index = -1
        for i in range(n):
            if l[i]!=r[i]:
                break
            else:
                min_index = i
        return l[min_index]
        
    def get_parent_list(self,node,parent_list):
        if node ==None:
            return
        parent_list.append(node)
        if node ==self.p or node == self.q:
            self.parent_list.append(list(parent_list))
        self.get_parent_list(node.left,parent_list)
        self.get_parent_list(node.right,parent_list)
        parent_list.pop()
        

sol = Solution()

# input
[6,2,8,0,4,7,9,null,null,3,5]
2
8
[6,2,8,0,4,7,9,null,null,3,5]
2
4
[2,1]
2
1

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
