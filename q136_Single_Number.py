from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result^=num
        return result

sol = Solution()


# input
nums = [2,2,1]
# output
output = sol.singleNumber(nums)
# answer
answer = 1
print(output, answer, answer == output)

# input
nums = [4,1,2,1,2]
# output
output = sol.singleNumber(nums)
# answer
answer = 4
print(output, answer, answer == output)

# input
nums = [1]
# output
output = sol.singleNumber(nums)
# answer
answer = 1
print(output, answer, answer == output)
