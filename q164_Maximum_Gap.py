from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2:
            return 0
        
        min_nums = min(nums)
        max_nums = max(nums)
        
        if min_nums == max_nums:
            return 0 
        
        average_gap = (max_nums-min_nums)/(n-1)
        
        buckets = [None]*n
        
        for num in nums:
            bucket_index = int((num-min_nums)/average_gap)
            if buckets[bucket_index] == None:
                buckets[bucket_index] = [num]
            else:
                if num < buckets[bucket_index][0]:
                    buckets[bucket_index].insert(0,num)
                if buckets[bucket_index][-1] < num:
                    buckets[bucket_index].append(num)

        last_elem = min_nums
        max_gap = 0
        
        for bucket in buckets:
            if bucket == None:
                continue
            gap_difference, last_elem = bucket[0] - last_elem, bucket[-1]
            if gap_difference > max_gap:
                max_gap = gap_difference
        return max_gap

sol = Solution()


# input
nums = [3,6,9,1]
# output
output = sol.maximumGap(nums)
# answer
answer = 3
print(output, answer, answer == output)

# input
nums = [10]
# output
output = sol.maximumGap(nums)
# answer
answer = 0
print(output, answer, answer == output)
