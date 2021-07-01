from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        subarray_sum = 0
        
        for num in nums:
            subarray_sum += num
            if subarray_sum>max_sum:
                max_sum = subarray_sum
            if subarray_sum < 0:
                subarray_sum = 0
        
        return max_sum

sol = Solution()


# input
nums = [-2,1,-3,4,-1,2,1,-5,4]
# output
output = sol.maxSubArray(nums)
# answer
answer = 6
print(output, answer, answer == output)

# input
nums = [1]
# output
output = sol.maxSubArray(nums)
# answer
answer = 1
print(output, answer, answer == output)

# input
nums = [-1]
# output
output = sol.maxSubArray(nums)
# answer
answer = -1
print(output, answer, answer == output)

# input
nums = [5,4,-1,7,8]
# output
output = sol.maxSubArray(nums)
# answer
answer = 23
print(output, answer, answer == output)

# input
nums = [-3,-2,-1]
# output
output = sol.maxSubArray(nums)
# answer
answer = -1
print(output, answer, answer == output)
