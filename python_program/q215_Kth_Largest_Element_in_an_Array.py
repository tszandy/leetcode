from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count
import queue

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

sol = Solution()

# input
nums = [3,2,1,5,6,4]

k = 2

# output
output = sol.findKthLargest(nums,k)
# answer
answer = 5
print(output, answer, answer == output)

# input
nums = [3,2,3,1,2,4,5,5,6]

k = 4

# output
output = sol.findKthLargest(nums,k)
# answer
answer = 4
print(output, answer, answer == output)
