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
    def removeDuplicates(self, nums: List[int]) -> int:
        record_elem = None
        n = len(nums)
        count_remove = 0
        r = 1
        while r < len(nums):
            if nums[r]==nums[r-1]: 
                if nums[r]!=record_elem:
                    record_elem = nums[r]
                    r+=1
                else:
                    count_remove +=1
                    nums.pop(r)
            else:
                r+=1
        return n - count_remove

sol = Solution()

# input
nums = [1]

# output
output = sol.removeDuplicates(nums)
# answer
answer = 1
print(output, answer, answer == output)

# input
nums = [1,1,1,2,2,3]

# output
output = sol.removeDuplicates(nums)
# answer
answer = 5
print(output, answer, answer == output)

# input
nums = [0,0,1,1,1,1,2,3,3]

# output
output = sol.removeDuplicates(nums)
# answer
answer = 7
print(output, answer, answer == output)
