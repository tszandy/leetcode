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
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        subarr_length = 0
        not_in_range_length = 0
        total_subarray = 0
        for num in nums:
            if num<=right:
                subarr_length+=1
                if left<=num:
                    not_in_range_length = 0
                else:
                    not_in_range_length +=1
                total_subarray+=subarr_length-not_in_range_length
            else:
                not_in_range_length = 0
                subarr_length = 0
        return total_subarray

sol = Solution()

# input
nums = [2,1,4,3]

left = 2

right = 3

# output
output = sol.numSubarrayBoundedMax(nums,left,right)
# answer
answer = 3
print(output, answer, answer == output)

# input
nums = [2,9,2,5,6]

left = 2

right = 8

# output
output = sol.numSubarrayBoundedMax(nums,left,right)
# answer
answer = 7
print(output, answer, answer == output)
