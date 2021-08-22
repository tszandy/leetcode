from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem = None
        count = 0
        
        for num in nums:
            if elem == num:
                count += 1
            elif elem!=num and count !=0:
                count -= 1
            else:
                elem = num
                count = 1
                
        return elem

sol = Solution()


# input
nums = [3,2,3]
# output
output = sol.majorityElement(nums)
# answer
answer = 3
print(output, answer, answer == output)

# input
nums = [2,2,1,1,1,2,2]
# output
output = sol.majorityElement(nums)
# answer
answer = 2
print(output, answer, answer == output)

# input
nums = [6,5,5]
# output
output = sol.majorityElement(nums)
# answer
answer = 5
print(output, answer, answer == output)
