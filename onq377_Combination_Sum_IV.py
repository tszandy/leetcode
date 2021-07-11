from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
#backtracking time limit exceed
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        nums.sort(key = lambda x:-x)
        count_combination = [0]
        
        def backtracking(count_sum,target):
            if count_sum > target:
                return
            if count_sum == target:
                count_combination[0]+=1
                return
            for num in nums:
                backtracking(count_sum+num,target)
                
        backtracking(0,target)
        return count_combination[0]

sol = Solution()


# input
nums = [1,2,3]

target = 4

# output
output = sol.combinationSum4(nums,target)
# answer
answer = 7
print(output, answer, answer == output)

# input
nums = [9]

target = 3

# output
output = sol.combinationSum4(nums,target)
# answer
answer = 0
print(output, answer, answer == output)
