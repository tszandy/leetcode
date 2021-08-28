from typing import List
from collections import Counter,defaultdict,deque
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count,zip_longest
import queue

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1]*nums[-2]-nums[0]*nums[1]

sol = Solution()

# input
nums = [5,6,2,7,4]

# output
output = sol.maxProductDifference(nums)
# answer
answer = 34
print(output, answer, answer == output)

# input
nums = [4,2,5,9,7,4,8]

# output
output = sol.maxProductDifference(nums)
# answer
answer = 64
print(output, answer, answer == output)
