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
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.count_sum = 0
        self.sum_numbers(root,"")
        return self.count_sum
        
        
    def sum_numbers(self,node,num_str):
        num_str+=str(node.val)
        if node.left == None and node.right == None:
            self.count_sum += int(num_str)
            return
        if node.left !=None:
            self.sum_numbers(node.left,num_str)
        if node.right !=None:
            self.sum_numbers(node.right,num_str)


sol = Solution()

# input
[0]
[1,2]
[1,2,3]
[4,9,0,5,1]
[0,1,2]

# output
output = sol.sumNumbers(root)
# answer
answer = ""
print(output, answer, answer == output)
