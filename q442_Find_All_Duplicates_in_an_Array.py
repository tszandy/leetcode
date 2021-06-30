from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return_list = []
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if num == -1:
                continue
            if i == num-1:
                continue
            else:
                nums[i]=-1
            while nums[num-1]!=num:
                swap = nums[num-1]
                nums[num-1]=num
                if swap == -1:
                    break
                num = swap
            else:
                return_list.append(num)
        return return_list                

sol = Solution()


# input
nums = [4,3,2,7,8,2,3,1]
# output
output = sol.findDuplicates(nums)
# answer
answer = [2,3]
print(output, answer, sorted(answer) == sorted(output))

# input
nums = [1,1,2]
# output
output = sol.findDuplicates(nums)
# answer
answer = [1]
print(output, answer, sorted(answer) == sorted(output))

# input
nums = [1]
# output
output = sol.findDuplicates(nums)
# answer
answer = []
print(output, answer, sorted(answer) == sorted(output))

# input
nums = [1,6,8,1,2,7,2,3,5,4]
# output
output = sol.findDuplicates(nums)
# answer
answer = [1,2]
print(output, answer, sorted(answer) == sorted(output))

# input
nums = [1,1]
# output
output = sol.findDuplicates(nums)
# answer
answer = [1]
print(output, answer, sorted(answer) == sorted(output))

# input
nums = [1,2]
# output
output = sol.findDuplicates(nums)
# answer
answer = []
print(output, answer, sorted(answer) == sorted(output))
