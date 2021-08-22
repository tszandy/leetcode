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
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.tree_sum_count = Counter()
        self.tree_sum(root)
        max_freq = max(self.tree_sum_count.values())
        return [key for key,val in self.tree_sum_count.items() if val == max_freq]

    def tree_sum(self,node):
        if node == None:
            return 0
        left_sum = self.tree_sum(node.left)
        right_sum = self.tree_sum(node.right)
        self.tree_sum_count[left_sum+right_sum+node.val]+=1
        return left_sum+right_sum+node.val


sol = Solution()

# input
[5,2,-3]
[5,2,-5]

# output
output = sol.findFrequentTreeSum(root)
# answer
answer = ""
print(output, answer, answer == output)
