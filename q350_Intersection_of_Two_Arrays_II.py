from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_1_counter = Counter(nums1)
        nums_2_counter = Counter(nums2)
        
        return_list = []
        for i in nums_1_counter:
            if i in nums_2_counter:
                return_list = return_list+[i]*min(nums_1_counter[i],nums_2_counter[i])
        return return_list

sol = Solution()


# input
nums1 = [1,2,2,1]
nums2 = [2,2]
# output
output = sol.intersect(nums1,nums2)
# answer
answer = [2,2]
print(output, answer, sorted(answer) == sorted(output))

# input
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
# output
output = sol.intersect(nums1,nums2)
# answer
answer = [4,9]
print(output, answer, sorted(answer) == sorted(output))
