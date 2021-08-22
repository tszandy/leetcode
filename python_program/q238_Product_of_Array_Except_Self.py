from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count_zero = len(list(filter(lambda x:x==0,nums)))
        if count_zero >= 2:
            return [0]*n
        if count_zero == 1:
            zero_index = nums.index(0)
            product = reduce(lambda x,y:x*y,nums[:zero_index]+nums[zero_index+1:])
            return [0]*zero_index+[product]+[0]*(n-zero_index-1)
        if count_zero == 0:
            product = reduce(lambda x,y:x*y,nums)
            return list(map(lambda x:product//x,nums))

sol = Solution()


# input
nums = [1,2,3,4]
# output
output = sol.productExceptSelf(nums)
# answer
answer = [24,12,8,6]
print(output, answer, answer == output)

# input
nums = [-1,1,0,-3,3]
# output
output = sol.productExceptSelf(nums)
# answer
answer = [0,0,9,0,0]
print(output, answer, answer == output)

# input
nums = [1,0,0,4]
# output
output = sol.productExceptSelf(nums)
# answer
answer = [0,0,0,0]
print(output, answer, answer == output)
