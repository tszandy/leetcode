from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return min(nums[0],nums[1])

        left_list_min = nums[0]
        half_index =len(nums)//2
        if left_list_min>nums[half_index]:
            finded_min = self.findMin(nums[:half_index+1])
        else:
            finded_min = self.findMin(nums[half_index+1:])

        if finded_min!=None:
            return min(finded_min,left_list_min)
        else:
            return left_list_min

sol = Solution()


# input
nums = [3,4,5,1,2]
# output
output = sol.findMin(nums)
# answer
answer = 1
print(output, answer, answer == output)

# input
nums = [4,5,6,7,0,1,2]
# output
output = sol.findMin(nums)
# answer
answer = 0
print(output, answer, answer == output)

# input
nums = [11,13,15,17]
# output
output = sol.findMin(nums)
# answer
answer = 11
print(output, answer, answer == output)

# input
nums = [2,1]
# output
output = sol.findMin(nums)
# answer
answer = 1
print(output, answer, answer == output)

# input
nums = [1,2]
# output
output = sol.findMin(nums)
# answer
answer = 1
print(output, answer, answer == output)
