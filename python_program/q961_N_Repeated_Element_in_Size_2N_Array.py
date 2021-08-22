from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for k in range(1,4):
            for i in range(len(nums)-k):
                if nums[i] == nums[i+k]:
                    return nums[i]

sol = Solution()


# input
nums = [1,2,3,3]
# output
output = sol.repeatedNTimes(nums)
# answer
answer = 3
print(output, answer, answer == output)

# input
nums = [2,1,2,5,3,2]
# output
output = sol.repeatedNTimes(nums)
# answer
answer = 2
print(output, answer, answer == output)

# input
nums = [5,1,5,2,5,3,5,4]
# output
output = sol.repeatedNTimes(nums)
# answer
answer = 5
print(output, answer, answer == output)
