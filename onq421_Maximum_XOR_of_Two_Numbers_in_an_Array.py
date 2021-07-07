from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:        
        max_xor = 0
        n = len(nums)
        if n == 1:
            return nums[0]
        
        for i in range(n):
            x = nums[i]
            for j in range(i+1,n):
                y = nums[j]
                max_xor = max(max_xor,x^y)
                
        return max_xor

sol = Solution()


# input
nums = [3,10,5,25,2,8]
# output
output = sol.findMaximumXOR(nums)
# answer
answer = 28
print(output, answer, answer == output)

# input
nums = [0]
# output
output = sol.findMaximumXOR(nums)
# answer
answer = 0
print(output, answer, answer == output)

# input
nums = [1]
# output
output = sol.findMaximumXOR(nums)
# answer
answer = 0
print(output, answer, answer == output)

# input
nums = [2,4]
# output
output = sol.findMaximumXOR(nums)
# answer
answer =6
print(output, answer, answer == output)

# input
nums = [8,10,2]
# output
output = sol.findMaximumXOR(nums)
# answer
answer = 10
print(output, answer, answer == output)

# input
nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# output
output = sol.findMaximumXOR(nums)
# answer
answer = 127
print(output, answer, answer == output)
