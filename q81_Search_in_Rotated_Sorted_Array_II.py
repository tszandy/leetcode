from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count
import queue
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return False
        L = 0
        R = len(nums)-1
        mid = int((L + R)/2)
        if nums[mid]==target:
            return True
        if nums[mid]<nums[R]:
            result_1 = self.search(nums[:mid],target)
            result_2 =  self.binary_search(nums[mid+1:],target)
        elif nums[mid] == nums[R]:
            result_1 = self.search(nums[:mid],target)
            result_2 =  self.search(nums[mid+1:],target)
        else:
            result_1 = self.binary_search(nums[:mid],target)
            result_2 =  self.search(nums[mid+1:],target)
        return result_1 or result_2

    def binary_search(self, nums:List[int], target:int) -> int:
        if len(nums) == 0:
            return False
        L = 0
        R = len(nums)-1
        mid = int((L + R)/2)
        if nums[mid] == target:
            return True
        if target < nums[mid]:
            return self.binary_search(nums[:mid],target)
        return self.binary_search(nums[mid+1:],target)

sol = Solution()

# input
nums = [2,2,2,3,2,2,2]

target = 3

# output
output = sol.search(nums,target)
# answer
answer = True
print(output, answer, answer == output)

# input
nums = [2,5,6,0,0,1,2]

target = 0

# output
output = sol.search(nums,target)
# answer
answer = True
print(output, answer, answer == output)

# input
nums = [2,5,6,0,0,1,2]

target = 3

# output
output = sol.search(nums,target)
# answer
answer = False
print(output, answer, answer == output)

# input
nums = [3,1]

target = 2

# output
output = sol.search(nums,target)
# answer
answer = False
print(output, answer, answer == output)

# input
nums = [1]

target = 0

# output
output = sol.search(nums,target)
# answer
answer = False
print(output, answer, answer == output)

# input
nums = [1]

target = 1

# output
output = sol.search(nums,target)
# answer
answer = True
print(output, answer, answer == output)
