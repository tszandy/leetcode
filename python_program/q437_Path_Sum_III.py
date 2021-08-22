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
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.path_sum_counter_by_node = defaultdict(Counter)
        self.path_sum_counter = Counter()
        self.targetSum = targetSum
        self.path_sum(root)
        return self.path_sum_counter_by_node[root][targetSum]+self.path_sum_counter[targetSum]
        
    def path_sum(self,node):
        if node == None:
            return
        if node.left!=None:
            self.path_sum(node.left)
            for key,val in self.path_sum_counter_by_node[node.left].items():
                self.path_sum_counter[key]+=val
                self.path_sum_counter_by_node[node][key+node.val]+=val
        if node.right!=None:
            self.path_sum(node.right)
            for key,val in self.path_sum_counter_by_node[node.right].items():
                self.path_sum_counter[key]+=val
                self.path_sum_counter_by_node[node][key+node.val]+=val
        self.path_sum_counter_by_node[node][node.val]+=1

sol = Solution()

# input
[1,2,3,4,5,6,7]
8
[10,5,-3,3,2,null,11,3,-2,null,1]
8
[5,4,8,11,null,13,4,7,2,null,null,5,1]
22
[1,-2,-3,1,3,-2,null,-1]
-1
# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
