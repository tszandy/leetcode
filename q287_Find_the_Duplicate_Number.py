from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
#Floyd's Tortoise and Hare (Cycle Detection)
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]
        # F+a = 2*(F+a)-nC for n\in{\mathbb{N}_{>=1}},C period of cycle
        # F+a = nC
        # F = nC-a
        # 0+F = a+nC-a mod C
        # 0 = 0 mod C entrance point
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare

#arithemetic sum wrong answer 
    def findDuplicate_1(self, nums: List[int]) -> int:
        n = len(nums)-1
        sum_nums = sum(nums)
        return sum_nums - (1+n)*n//2


sol = Solution()


# input
nums = [1,3,4,2,2]
# output
output = sol.findDuplicate(nums)
# answer
answer = 2
print(output, answer, answer == output)

# input
nums = nums = [3,1,3,4,2]
# output
output = sol.findDuplicate(nums)
# answer
answer = 3
print(output, answer, answer == output)

# input
nums = [1,1]
# output
output = sol.findDuplicate(nums)
# answer
answer = 1
print(output, answer, answer == output)

# input
nums = [1,1,2]
# output
output = sol.findDuplicate(nums)
# answer
answer = 1
print(output, answer, answer == output)

# input
nums = [2,2,2,2,2]
# output
output = sol.findDuplicate(nums)
# answer
answer = 2
print(output, answer, answer == output)
