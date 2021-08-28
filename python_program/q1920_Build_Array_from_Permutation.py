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
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]

sol = Solution()

# input
[0,2,1,5,3,4]
[5,0,1,2,3,4]

# output
output = sol.buildArray(nums)
# answer
answer = ""
print(output, answer, answer == output)
