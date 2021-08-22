from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        index = bisect_left(nums,target)
        if n == index:
            return -1
        elif nums[index]!=target:
            return -1
        else:
            return index

sol = Solution()

# input
nums = [-1,0,3,5,9,12]

target = 9

# output
output = sol.search(nums, target)
# answer
answer = 4
print(output, answer, answer == output)

# input
nums = [-1,0,3,5,9,12]

target = 2

# output
output = sol.search(nums, target)
# answer
answer = -1
print(output, answer, answer == output)
