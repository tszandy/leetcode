from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count
import queue

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return_set = set([()])
        
        for num in nums:
            for t in list(return_set):
                return_set.add(t+(num,))
        return list(map(lambda x:list(x),return_set))


sol = Solution()

# input
nums = [1,2,2]

# output
output = sol.subsetsWithDup(nums)
# answer
answer = [[1,2],[2],[1],[1,2,2],[2,2],[]]

print(output, answer, sorted(answer) == sorted(output))

# input
nums = [0]

# output
output = sol.subsetsWithDup(nums)
# answer
answer = [[0],[]]

print(output, answer, sorted(answer) == sorted(output))
