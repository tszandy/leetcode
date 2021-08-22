from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n <3:
            return 0
        
        difference_list = []
        for i in range(1,n):
            difference_list.append(nums[i]-nums[i-1])
        count_arithemetic_slice = -1
        count_arithemetic_list = []
        for i in range(1,n-1):
            if difference_list[i]==difference_list[i-1]:
                if count_arithemetic_slice == -1:
                    count_arithemetic_slice=3
                else:
                    count_arithemetic_slice+=1
            else:
                if count_arithemetic_slice == -1:
                    continue
                else:
                    count_arithemetic_list.append(count_arithemetic_slice)
                    count_arithemetic_slice = -1

        if count_arithemetic_slice != -1:
            count_arithemetic_list.append(count_arithemetic_slice)
            count_arithemetic_slice = -1
        
        count_arithemetic_slices = 0
        
        for i in count_arithemetic_list:
            count_arithemetic_slices+=(i-1)*(i-2)//2
        return count_arithemetic_slices

sol = Solution()


# input
nums = [1,2,3]
# output
output = sol.numberOfArithmeticSlices(nums)
# answer
answer = 1
print(output, answer, answer == output)

# input
nums = [1,2,3,4]
# output
output = sol.numberOfArithmeticSlices(nums)
# answer
answer = 3
print(output, answer, answer == output)

# input
nums = [1]
# output
output = sol.numberOfArithmeticSlices(nums)
# answer
answer = 0
print(output, answer, answer == output)

# input
nums = [1,2,5,3,4,3,4,5,6,1,2,3,4,2,1,2,3,4,5,7,4,5,6,7]
# output
output = sol.numberOfArithmeticSlices(nums)
# answer
answer = 15
print(output, answer, answer == output)
