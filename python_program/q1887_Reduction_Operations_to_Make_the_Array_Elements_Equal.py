from typing import List
from collections import Counter,defaultdict,deque
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count,zip_longest
import queue

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        pre_num = None
        operations_for_i = -1
        count_operations = 0
        for num in nums:
            if pre_num !=num:
                pre_num = num
                operations_for_i+=1
            count_operations+= operations_for_i
        return count_operations

sol = Solution()

# input
nums = [5,1,3]

# output
output = sol.reductionOperations(nums)
# answer
answer = 3
print(output, answer, answer == output)

# input
nums = [1,1,1]

# output
output = sol.reductionOperations(nums)
# answer
answer = 0
print(output, answer, answer == output)

# input
nums = [1,1,2,2,3]

# output
output = sol.reductionOperations(nums)
# answer
answer = 4
print(output, answer, answer == output)
