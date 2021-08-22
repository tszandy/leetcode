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
            return -1
        L = 0
        R = len(nums)-1
        mid = int((L + R)/2)
        while L<R:
            if nums[mid]<nums[R]:
                R = mid
            else:
                L = mid + 1
            mid = int((L + R)/2)

        result1 = self.binary_search(nums[:mid],target)
        if result1 != -1:
            return result1
        else:
            result2 = self.binary_search(nums[mid:],target)
            if result2 != -1:
                return mid + result2
            else:
                return -1

    def binary_search(self, nums:List[int], target:int) -> int:
        if len(nums) == 0:
            return -1
        L = 0
        R = len(nums)-1
        mid = int((L + R)/2)
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            return self.binary_search(nums[:mid],target)
        result = self.binary_search(nums[mid+1:],target)
        if result != -1:
            return result + mid + 1
        return -1

sol = Solution()

# input
nums = [4,5,6,7,0,1,2]

target = 0

# output
output = sol.search(nums,target)
# answer
answer = 4
print(output, answer, answer == output)

# input
nums = [4,5,6,7,0,1,2]

target = 3

# output
output = sol.search(nums,target)
# answer
answer = -1
print(output, answer, answer == output)

# input
nums = [3,1]

target = 2

# output
output = sol.search(nums,target)
# answer
answer = -1
print(output, answer, answer == output)

# input
nums = [1]

target = 0

# output
output = sol.search(nums,target)
# answer
answer = -1
print(output, answer, answer == output)

# input
nums = [1]

target = 1

# output
output = sol.search(nums,target)
# answer
answer = 0
print(output, answer, answer == output)
