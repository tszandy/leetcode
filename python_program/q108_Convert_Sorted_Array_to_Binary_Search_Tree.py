from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        half_index = len(nums) // 2
        
        return TreeNode(nums[half_index],self.sortedArrayToBST(nums[:half_index]),self.sortedArrayToBST(nums[half_index+1:]))

sol = Solution()


# input
nums = [-10,-3,0,5,9]
# output
output = sol.sortedArrayToBST(nums)
# answer
answer = [0,-3,9,-10,null,5]
print(output, answer, answer == output)
