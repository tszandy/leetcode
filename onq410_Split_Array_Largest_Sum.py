from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
from bisect import bisect_left

import numpy as np
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        nums_sum = sum(nums)
        average = nums_sum/m
        
        nums_cum_sum = np.cumsum(nums)
        l = 0
        r = n-1

        def split_array(l,r,m):
            if m>r-l+1:
                return float("inf")
                
            if m ==1:
                if l == 0:
                    return nums_cum_sum[r]
                else:
                    return nums_cum_sum[r] - nums_cum_sum[l-1]
            for i in range(l,r+1):
                minus_sum = 0
                if l!=0:
                    minus_sum = nums_cum_sum[l-1]
                sum_first_arr = nums_cum_sum[i]-minus_sum
                if sum_first_arr>average:
                    max_1 = max(sum_first_arr,split_array(i+1,r,m-1))
                    max_2 = max(nums_cum_sum[i-1]-minus_sum,split_array(i,r,m-1))
                    return min(max_1,max_2)
            return float("inf")
        return split_array(l,r,m)

sol = Solution()


# input
nums = [7,2,5,10,8]

m = 2

# output
output = sol.splitArray(nums,m)
# answer
answer = 18
print(output, answer, answer == output)

# input
nums = [7,2,5,10,8]

m = 5

# output
output = sol.splitArray(nums,m)
# answer
answer = 10
print(output, answer, answer == output)

# input
nums = [7,2,5,10,8,7,2,5,10,8,7,2,5,10,8,7,2,5,10,8,7,2,5,10,8]

m = 5

# output
output = sol.splitArray(nums,m)
# answer
answer = 32
print(output, answer, answer == output)

# input
nums = [1,2,3,4,5]

m = 2

# output
output = sol.splitArray(nums,m)
# answer
answer = 9
print(output, answer, answer == output)

# input
nums = [1,4,4]

m = 3

# output
output = sol.splitArray(nums,m)
# answer
answer = 4
print(output, answer, answer == output)

# input
nums = [7,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,8,7,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,8,7,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,8,7,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,8,7,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,8,7,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,87,2,5,10,8]

m = 30

# output
output = sol.splitArray(nums,m)
# answer
answer = 18
print(output, answer, answer == output)
