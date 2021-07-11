from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        n = len(nums)
        rotation_sum = sum(map(lambda x:x[0]*x[1],zip(nums,range(n))))
        
        return_sum = rotation_sum
        for num in nums[::-1]:
            rotation_sum = rotation_sum+sum_nums-n*(num)
            return_sum = max(return_sum,rotation_sum)
            
        return return_sum

sol = Solution()


# input
nums = [4,3,2,6]

# output
output = sol.maxRotateFunction(nums)
# answer
answer = 26
print(output, answer, answer == output)

# input
nums = [1000000007]

# output
output = sol.maxRotateFunction(nums)
# answer
answer = 0
print(output, answer, answer == output)

# input
nums = [1,2,3,4,5,6,7,8,9,10]

# output
output = sol.maxRotateFunction(nums)
# answer
answer = 330
print(output, answer, answer == output)
