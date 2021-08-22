from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums)==0:
            return None
        index = nums.index(max(nums))
        return TreeNode(val = nums[index],left = self.constructMaximumBinaryTree(nums[:index]),right = self.constructMaximumBinaryTree(nums[index+1:]))

sol = Solution()

# input
nums = [3,2,1,6,0,5]

# output
output = sol.constructMaximumBinaryTree(nums)
# answer
answer = ""
print(output, answer, answer == output)

# input
nums = [3,2,1]

# output
output = sol.constructMaximumBinaryTree(nums)
# answer
answer = ""
print(output, answer, answer == output)
