from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
#backtracking_time_limit_excess
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if sum(nums)%2==1:
            return False
        
        
        def backtracking(index=0,list_sum=0,target=sum(nums)//2):
            if list_sum == target:
                return True
            if list_sum>target:
                return False
            
            for i in range(index,n):
                num = nums[i]
                if backtracking(i+1,list_sum+num,target):
                    return True
            return False

        return backtracking()

sol = Solution()


# input
nums = [1,5,11,5]
# output
output = sol.canPartition(nums)
# answer
answer = True
print(output, answer, answer == output)

# input
nums = [1,2,3,5]
# output
output = sol.canPartition(nums)
# answer
answer = False
print(output, answer, answer == output)
