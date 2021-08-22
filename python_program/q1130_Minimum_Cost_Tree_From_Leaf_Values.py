from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @lru_cache(None)
        def get_sum_and_max(arr):
            n = len(arr)
            if len(arr)==1:
                return (0,arr[0])
            if len(arr)==2:
                return (arr[0]*arr[1],max(arr[0],arr[1]))
            
            min_sum,max_elem = float("inf"),0
            for i in range(1,n):
                left_min_sum ,left_max_elem = get_sum_and_max(arr[:i])
                right_min_sum,right_max_elem = get_sum_and_max(arr[i:])
                min_sum = min(min_sum,left_min_sum+right_min_sum+left_max_elem*right_max_elem)
                max_elem = max(left_max_elem,right_max_elem)
            
            return min_sum,max_elem
        max_sum,_ = get_sum_and_max(tuple(arr))
        return max_sum

sol = Solution()


# input
arr = [1,2]

# output
output = sol.mctFromLeafValues(arr)
# answer
answer = 2
print(output, answer, answer == output)

# input
arr = [6,2,4]

# output
output = sol.mctFromLeafValues(arr)
# answer
answer = 32
print(output, answer, answer == output)

# input
arr = [6,2,11,2,3,4,1,5,12,3,4,2,1]

# output
output = sol.mctFromLeafValues(arr)
# answer
answer = 377
print(output, answer, answer == output)

# input
arr = [6,2,11,2,3,4,1,5,12,3,4,2,1,1,2,3,5,1,2,3,5,2,13,7]

# output
output = sol.mctFromLeafValues(arr)
# answer
answer = 729
print(output, answer, answer == output)

# input
arr = [6,2,11,2,3,4,1,5,12,3,4,2,1,1,2,1,5,12,3,4,2,1,1,2,3,5,1,2,3,5,2,13,7,1,2,2,1,4,1,5]

# output
output = sol.mctFromLeafValues(arr)
# answer
answer = 1057
print(output, answer, answer == output)
