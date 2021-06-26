from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            x = nums[i]
            nums[i] = 0
            while True:
                if x<=0 or x>n or nums[x-1]==x:
                    break
                y = nums[x-1]
                nums[x-1]=x
                x=y
        
        for i in range(n):
            if nums[i] == 0:
                return i+1
        return n+1    
            

sol = Solution()


# input
nums = [1,2,0]
# output
output = sol.firstMissingPositive(nums)
# answer
answer = 3
print(output, answer, answer == output)

# input
nums = [3,4,-1,1]
# output
output = sol.firstMissingPositive(nums)
# answer
answer = 2
print(output, answer, answer == output)

# input
nums = [7,8,9,11,12]
# output
output = sol.firstMissingPositive(nums)
# answer
answer = 1
print(output, answer, answer == output)
