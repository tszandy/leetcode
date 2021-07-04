from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return list(sum(zip(nums[:n],nums[n:]),()))

sol = Solution()


# input
nums = [2,5,1,3,4,7]
n = 3
# output
output = sol.shuffle(nums,n)
# answer
answer = [2,3,5,4,1,7] 
print(output, answer, answer == output)

# input
nums = [1,2,3,4,4,3,2,1]
n = 4
# output
output = sol.shuffle(nums,n)
# answer
answer = [1,4,2,3,3,2,4,1]
print(output, answer, answer == output)

# input
nums = [1,1,2,2,]
n = 2
# output
output = sol.shuffle(nums,n)
# answer
answer = [1,2,1,2] 
print(output, answer, answer == output)
