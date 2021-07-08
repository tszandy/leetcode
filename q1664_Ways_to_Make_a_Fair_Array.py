from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        even_index_sum = reduce(lambda x,y:x+y,map(lambda x:x[0]*x[1],zip(map(lambda x:x%2==0,range(n)),nums)))
        odd_index_sum = reduce(lambda x,y:x+y,map(lambda x:x[0]*x[1],zip(map(lambda x:x%2==1,range(n)),nums)))
        
        prior_even_sum = 0
        prior_odd_sum  = 0
        
        count_fair_array = 0
        for i in range(n):
            num = nums[i]
            if i %2==0:
                if prior_even_sum+odd_index_sum == prior_odd_sum+even_index_sum-num:
                    count_fair_array+=1
                prior_even_sum += num
                even_index_sum -= num
            else:
                if prior_even_sum+odd_index_sum-num == prior_odd_sum+even_index_sum:
                    count_fair_array+=1
                prior_odd_sum += num
                odd_index_sum -= num
        return count_fair_array

sol = Solution()


# input
nums = [2,1,6,4]
# output
output = sol.waysToMakeFair(nums)
# answer
answer = 1
print(output, answer, answer == output)

# input
nums = [1,1,1]
# output
output = sol.waysToMakeFair(nums)
# answer
answer = 3
print(output, answer, answer == output)

# input
nums = [1,2,3]
# output
output = sol.waysToMakeFair(nums)
# answer
answer = 0
print(output, answer, answer == output)

# input
nums = [1]
# output
output = sol.waysToMakeFair(nums)
# answer
answer = 1
print(output, answer, answer == output)
