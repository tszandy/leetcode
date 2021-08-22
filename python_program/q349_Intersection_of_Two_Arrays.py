from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        return list(set.intersection(set_1,set_2))

sol = Solution()


# input
nums1 = [1,2,2,1]
nums2 = [2,2]
# output
output = sol.intersection(nums1,nums2)
# answer
answer = [2]
print(output, answer, sorted(answer) == sorted(output))

# input
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
# output
output = sol.intersection(nums1,nums2)
# answer
answer = [9,4]
print(output, answer, sorted(answer) == sorted(output))
