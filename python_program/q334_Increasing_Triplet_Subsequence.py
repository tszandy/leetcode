from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        record_1 = (float("inf"),-1)
        record_2_l = None
        record_2_r = None
        for i,e in enumerate(nums):
            if record_2_r and record_2_r[0] < e:
                return True
            if record_2_r and e>record_1[0] and e<record_2_r[0]:
                record_2_l = record_1
                record_2_r = (e,i)
            
            if e > record_1[0] and not record_2_r:
                record_2_l = record_1
                record_2_r = (e,i)
            
            if e<record_1[0]:
                record_1 = (e,i)
            
        return False

sol = Solution()


# input
nums = [1,2,3,4,5]
# output
output = sol.increasingTriplet(nums)
# answer
answer = True
print(output, answer, answer == output)

# input
nums = [5,4,3,2,1]
# output
output = sol.increasingTriplet(nums)
# answer
answer = False
print(output, answer, answer == output)

# input
nums = [2,1,5,0,4,6]
# output
output = sol.increasingTriplet(nums)
# answer
answer = True
print(output, answer, answer == output)
