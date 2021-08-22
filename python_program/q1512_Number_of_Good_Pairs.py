from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        count = 0
        for v in nums_counter.values():
            count += v*(v-1)//2
        return count

sol = Solution()


# input
nums = [1,2,3,1,1,3]

# output
output = sol.numIdenticalPairs(nums)
# answer
answer = 4
print(output, answer, answer == output)

# input
nums = [1,1,1,1]

# output
output = sol.numIdenticalPairs(nums)
# answer
answer = 6
print(output, answer, answer == output)

# input
nums = [1,2,3]

# output
output = sol.numIdenticalPairs(nums)
# answer
answer = 0
print(output, answer, answer == output)
