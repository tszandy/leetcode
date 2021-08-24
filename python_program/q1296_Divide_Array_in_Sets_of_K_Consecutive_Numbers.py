from typing import List
from collections import Counter,defaultdict,deque
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count,zip_longest
import queue

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        n = len(nums)
        if n%k!=0:
            return False
        while nums:
            first_num = nums[0]
            for i in range(k):
                index = bisect_left(nums,first_num+i)
                if nums[index]!=first_num+i:
                    return False
                nums.pop(index)
        return True

sol = Solution()

# input
nums = [1,2,3,3,4,4,5,6]

k = 4

# output
output = sol.isPossibleDivide(nums,k)
# answer
answer = True
print(output, answer, answer == output)

# input
nums = [3,2,1,2,3,4,3,4,5,9,10,11]

k = 3

# output
output = sol.isPossibleDivide(nums,k)
# answer
answer = True
print(output, answer, answer == output)

# input
nums = [3,3,2,2,1,1]

k = 3

# output
output = sol.isPossibleDivide(nums,k)
# answer
answer = True
print(output, answer, answer == output)

# input
nums = [1,2,3,4]

k = 3

# output
output = sol.isPossibleDivide(nums,k)
# answer
answer = False
print(output, answer, answer == output)

# input
nums = [1,1,2,2,3,3]

k = 2

# output
output = sol.isPossibleDivide(nums,k)
# answer
answer = False
print(output, answer, answer == output)
