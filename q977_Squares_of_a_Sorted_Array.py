from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(map(lambda x:x**2,nums))


sol = Solution()


# input
nums = [-4,-1,0,3,10]
# output
output = sol.sortedSquares(nums)
# answer
answer = [0,1,9,16,100]
print(output, answer, answer == output)

# input
nums = [-7,-3,2,3,11]
# output
output = sol.sortedSquares(nums)
# answer
answer = [4,9,9,49,121]
print(output, answer, answer == output)
