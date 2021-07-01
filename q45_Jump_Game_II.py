from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def jump(self, nums: List[int]) -> int:
    	jump_count = 0
    	left, right = 1, min(nums[0], len(nums) - 1)
    	while left < len(nums):
    		new_right = right
    		for i in range(left, right+1):
    			new_right = max(new_right, i + nums[i])
    			new_right = min(new_right, len(nums) - 1)

    		jump_count +=1
    		left, right = right+1, new_right
    	return jump_count


# dp in n^2
    def jump_1(self, nums: List[int]) -> int:
        n = len(nums)
        jump_list = [float("inf")]*n
        jump_list[0]=0
        for i in range(1,n):
            for j in range(0,i):
                if (j+nums[j])>=i and jump_list[i]>jump_list[j]+1:
                    jump_list[i]=jump_list[j]+1
        return jump_list[-1]

sol = Solution()


# input
nums = [2,3,1,1,4]
# output
output = sol.jump(nums)
# answer
answer = 2
print(output, answer, answer == output)

# input
nums = [2,3,0,1,4]
# output
output = sol.jump(nums)
# answer
answer = 2
print(output, answer, answer == output)

# input
nums = [1,0]
# output
output = sol.jump(nums)
# answer
answer = 1
print(output, answer, answer == output)

# input
nums = [2,3,1,1,4,3,2,5,1,5,6,3,4,2,3,5,1]
# output
output = sol.jump(nums)
# answer
answer = 5
print(output, answer, answer == output)
