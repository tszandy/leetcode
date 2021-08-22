from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        arith_freq = [defaultdict(int) for _ in range(n)]

        for j in range(n):
            elem_2 = nums[j]
            for i in range(j):
                elem_1 = nums[i]
                diff = elem_2 - elem_1
                count += arith_freq[i][diff]
                arith_freq[j][diff] += 1 + arith_freq[i][diff]

        return count
                
                



sol = Solution()


# input
nums = [2,4,6,8,10]

# output
output = sol.numberOfArithmeticSlices(nums)
# answer
answer = 7
print(output, answer, answer == output)

# input
nums = [7,7,7,7,7]

# output
output = sol.numberOfArithmeticSlices(nums)
# answer
answer = 16
print(output, answer, answer == output)
