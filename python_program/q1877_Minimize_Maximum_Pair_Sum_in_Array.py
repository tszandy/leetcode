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
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        max_pair_sum = 0
        for i in range(n//2):
            max_pair_sum = max(max_pair_sum,nums[i]+nums[n-1-i])
        return max_pair_sum

sol = Solution()

# input
[3,5,2,3]
[3,5,4,2,4,6]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
