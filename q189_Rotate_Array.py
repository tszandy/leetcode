from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0,nums.pop())
        return nums

sol = Solution()


# input
nums = [1,2,3,4,5,6,7]
k = 3
# output
output = sol.rotate(nums,k)
# answer
answer = [5,6,7,1,2,3,4]
print(output, answer, answer == output)

# input
nums = [-1,-100,3,99]
k = 2
# output
output = sol.rotate(nums,k)
# answer
answer = [3,99,-1,-100]
print(output, answer, answer == output)

# input
nums = list(range(10**5))
k = 50
# output
output = sol.rotate(nums,k)
# answer
answer = list(range(10**5-50,10**5))+list(range(10**5-50))
print(output, answer, answer == output)

