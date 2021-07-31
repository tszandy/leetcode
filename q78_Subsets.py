from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return_list = [[]]
        for num in nums:
            for l in list(return_list):
                return_list.append(l+[num])
        return return_list

sol = Solution()

# input
nums = [0]
# output
output = sol.subsets(nums)
# answer
answer = [[],[0]]

print(output, answer, answer == output)

# input
nums = [0, 1]

# output
output = sol.subsets(nums)
# answer
answer = [[],[0],[1],[0,1]]
print(output, answer, answer == output)

# input
nums = [1,2,3]

# output
output = sol.subsets(nums)
# answer
answer = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

print(output, answer, answer == output)

# input
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# output
output = sol.subsets(nums)
# answer
answer = [[], [0], [1], [0, 1], [2], [0, 2], [1, 2], [0, 1, 2], [3], [0, 3], [1, 3], [0, 1, 3], [2, 3], [0, 2, 3], [1, 2, 3], [0, 1, 2, 3], [4], [0, 4], [1, 4], [0, 1, 4], [2, 4], [0, 2, 4], [1, 2, 4], [0, 1, 2, 4], [3, 4], [0, 3, 4], [1, 3, 4], [0, 1, 3, 4], [2, 3, 4], [0, 2, 3, 4], [1, 2, 3, 4], [0, 1, 2, 3, 4], [5], [0, 5], [1, 5], [0, 1, 5], [2, 5], [0, 2, 5], [1, 2, 5], [0, 1, 2, 5], [3, 5], [0, 3, 5], [1, 3, 5], [0, 1, 3, 5], [2, 3, 5], [0, 2, 3, 5], [1, 2, 3, 5], [0, 1, 2, 3, 5], [4, 5], [0, 4, 5], [1, 4, 5], [0, 1, 4, 5], [2, 4, 5], [0, 2, 4, 5], [1, 2, 4, 5], [0, 1, 2, 4, 5], [3, 4, 5], [0, 3, 4, 5], [1, 3, 4, 5], [0, 1, 3, 4, 5], [2, 3, 4, 5], [0, 2, 3, 4, 5], [1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [6], [0, 6], [1, 6], [0, 1, 6], [2, 6], [0, 2, 6], [1, 2, 6], [0, 1, 2, 6], [3, 6], [0, 3, 6], [1, 3, 6], [0, 1, 3, 6], [2, 3, 6], [0, 2, 3, 6], [1, 2, 3, 6], [0, 1, 2, 3, 6], [4, 6], [0, 4, 6], [1, 4, 6], [0, 1, 4, 6], [2, 4, 6], [0, 2, 4, 6], [1, 2, 4, 6], [0, 1, 2, 4, 6], [3, 4, 6], [0, 3, 4, 6], [1, 3, 4, 6], [0, 1, 3, 4, 6], [2, 3, 4, 6], [0, 2, 3, 4, 6], [1, 2, 3, 4, 6], [0, 1, 2, 3, 4, 6], [5, 6], [0, 5, 6], [1, 5, 6], [0, 1, 5, 6], [2, 5, 6], [0, 2, 5, 6], [1, 2, 5, 6], [0, 1, 2, 5, 6], [3, 5, 6], [0, 3, 5, 6], [1, 3, 5, 6], [0, 1, 3, 5, 6], [2, 3, 5, 6], [0, 2, 3, 5, 6], [1, 2, 3, 5, 6], [0, 1, 2, 3, 5, 6], [4, 5, 6], [0, 4, 5, 6], [1, 4, 5, 6], [0, 1, 4, 5, 6], [2, 4, 5, 6], [0, 2, 4, 5, 6], [1, 2, 4, 5, 6], [0, 1, 2, 4, 5, 6], [3, 4, 5, 6], [0, 3, 4, 5, 6], [1, 3, 4, 5, 6], [0, 1, 3, 4, 5, 6], [2, 3, 4, 5, 6], [0, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6], [7], [0, 7], [1, 7], [0, 1, 7], [2, 7], [0, 2, 7], [1, 2, 7], [0, 1, 2, 7], [3, 7], [0, 3, 7], [1, 3, 7], [0, 1, 3, 7], [2, 3, 7], [0, 2, 3, 7], [1, 2, 3, 7], [0, 1, 2, 3, 7], [4, 7], [0, 4, 7], [1, 4, 7], [0, 1, 4, 7], [2, 4, 7], [0, 2, 4, 7], [1, 2, 4, 7], [0, 1, 2, 4, 7], [3, 4, 7], [0, 3, 4, 7], [1, 3, 4, 7], [0, 1, 3, 4, 7], [2, 3, 4, 7], [0, 2, 3, 4, 7], [1, 2, 3, 4, 7], [0, 1, 2, 3, 4, 7], [5, 7], [0, 5, 7], [1, 5, 7], [0, 1, 5, 7], [2, 5, 7], [0, 2, 5, 7], [1, 2, 5, 7], [0, 1, 2, 5, 7], [3, 5, 7], [0, 3, 5, 7], [1, 3, 5, 7], [0, 1, 3, 5, 7], [2, 3, 5, 7], [0, 2, 3, 5, 7], [1, 2, 3, 5, 7], [0, 1, 2, 3, 5, 7], [4, 5, 7], [0, 4, 5, 7], [1, 4, 5, 7], [0, 1, 4, 5, 7], [2, 4, 5, 7], [0, 2, 4, 5, 7], [1, 2, 4, 5, 7], [0, 1, 2, 4, 5, 7], [3, 4, 5, 7], [0, 3, 4, 5, 7], [1, 3, 4, 5, 7], [0, 1, 3, 4, 5, 7], [2, 3, 4, 5, 7], [0, 2, 3, 4, 5, 7], [1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 7], [6, 7], [0, 6, 7], [1, 6, 7], [0, 1, 6, 7], [2, 6, 7], [0, 2, 6, 7], [1, 2, 6, 7], [0, 1, 2, 6, 7], [3, 6, 7], [0, 3, 6, 7], [1, 3, 6, 7], [0, 1, 3, 6, 7], [2, 3, 6, 7], [0, 2, 3, 6, 7], [1, 2, 3, 6, 7], [0, 1, 2, 3, 6, 7], [4, 6, 7], [0, 4, 6, 7], [1, 4, 6, 7], [0, 1, 4, 6, 7], [2, 4, 6, 7], [0, 2, 4, 6, 7], [1, 2, 4, 6, 7], [0, 1, 2, 4, 6, 7], [3, 4, 6, 7], [0, 3, 4, 6, 7], [1, 3, 4, 6, 7], [0, 1, 3, 4, 6, 7], [2, 3, 4, 6, 7], [0, 2, 3, 4, 6, 7], [1, 2, 3, 4, 6, 7], [0, 1, 2, 3, 4, 6, 7], [5, 6, 7], [0, 5, 6, 7], [1, 5, 6, 7], [0, 1, 5, 6, 7], [2, 5, 6, 7], [0, 2, 5, 6, 7], [1, 2, 5, 6, 7], [0, 1, 2, 5, 6, 7], [3, 5, 6, 7], [0, 3, 5, 6, 7], [1, 3, 5, 6, 7], [0, 1, 3, 5, 6, 7], [2, 3, 5, 6, 7], [0, 2, 3, 5, 6, 7], [1, 2, 3, 5, 6, 7], [0, 1, 2, 3, 5, 6, 7], [4, 5, 6, 7], [0, 4, 5, 6, 7], [1, 4, 5, 6, 7], [0, 1, 4, 5, 6, 7], [2, 4, 5, 6, 7], [0, 2, 4, 5, 6, 7], [1, 2, 4, 5, 6, 7], [0, 1, 2, 4, 5, 6, 7], [3, 4, 5, 6, 7], [0, 3, 4, 5, 6, 7], [1, 3, 4, 5, 6, 7], [0, 1, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7], [0, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7], [8], [0, 8], [1, 8], [0, 1, 8], [2, 8], [0, 2, 8], [1, 2, 8], [0, 1, 2, 8], [3, 8], [0, 3, 8], [1, 3, 8], [0, 1, 3, 8], [2, 3, 8], [0, 2, 3, 8], [1, 2, 3, 8], [0, 1, 2, 3, 8], [4, 8], [0, 4, 8], [1, 4, 8], [0, 1, 4, 8], [2, 4, 8], [0, 2, 4, 8], [1, 2, 4, 8], [0, 1, 2, 4, 8], [3, 4, 8], [0, 3, 4, 8], [1, 3, 4, 8], [0, 1, 3, 4, 8], [2, 3, 4, 8], [0, 2, 3, 4, 8], [1, 2, 3, 4, 8], [0, 1, 2, 3, 4, 8], [5, 8], [0, 5, 8], [1, 5, 8], [0, 1, 5, 8], [2, 5, 8], [0, 2, 5, 8], [1, 2, 5, 8], [0, 1, 2, 5, 8], [3, 5, 8], [0, 3, 5, 8], [1, 3, 5, 8], [0, 1, 3, 5, 8], [2, 3, 5, 8], [0, 2, 3, 5, 8], [1, 2, 3, 5, 8], [0, 1, 2, 3, 5, 8], [4, 5, 8], [0, 4, 5, 8], [1, 4, 5, 8], [0, 1, 4, 5, 8], [2, 4, 5, 8], [0, 2, 4, 5, 8], [1, 2, 4, 5, 8], [0, 1, 2, 4, 5, 8], [3, 4, 5, 8], [0, 3, 4, 5, 8], [1, 3, 4, 5, 8], [0, 1, 3, 4, 5, 8], [2, 3, 4, 5, 8], [0, 2, 3, 4, 5, 8], [1, 2, 3, 4, 5, 8], [0, 1, 2, 3, 4, 5, 8], [6, 8], [0, 6, 8], [1, 6, 8], [0, 1, 6, 8], [2, 6, 8], [0, 2, 6, 8], [1, 2, 6, 8], [0, 1, 2, 6, 8], [3, 6, 8], [0, 3, 6, 8], [1, 3, 6, 8], [0, 1, 3, 6, 8], [2, 3, 6, 8], [0, 2, 3, 6, 8], [1, 2, 3, 6, 8], [0, 1, 2, 3, 6, 8], [4, 6, 8], [0, 4, 6, 8], [1, 4, 6, 8], [0, 1, 4, 6, 8], [2, 4, 6, 8], [0, 2, 4, 6, 8], [1, 2, 4, 6, 8], [0, 1, 2, 4, 6, 8], [3, 4, 6, 8], [0, 3, 4, 6, 8], [1, 3, 4, 6, 8], [0, 1, 3, 4, 6, 8], [2, 3, 4, 6, 8], [0, 2, 3, 4, 6, 8], [1, 2, 3, 4, 6, 8], [0, 1, 2, 3, 4, 6, 8], [5, 6, 8], [0, 5, 6, 8], [1, 5, 6, 8], [0, 1, 5, 6, 8], [2, 5, 6, 8], [0, 2, 5, 6, 8], [1, 2, 5, 6, 8], [0, 1, 2, 5, 6, 8], [3, 5, 6, 8], [0, 3, 5, 6, 8], [1, 3, 5, 6, 8], [0, 1, 3, 5, 6, 8], [2, 3, 5, 6, 8], [0, 2, 3, 5, 6, 8], [1, 2, 3, 5, 6, 8], [0, 1, 2, 3, 5, 6, 8], [4, 5, 6, 8], [0, 4, 5, 6, 8], [1, 4, 5, 6, 8], [0, 1, 4, 5, 6, 8], [2, 4, 5, 6, 8], [0, 2, 4, 5, 6, 8], [1, 2, 4, 5, 6, 8], [0, 1, 2, 4, 5, 6, 8], [3, 4, 5, 6, 8], [0, 3, 4, 5, 6, 8], [1, 3, 4, 5, 6, 8], [0, 1, 3, 4, 5, 6, 8], [2, 3, 4, 5, 6, 8], [0, 2, 3, 4, 5, 6, 8], [1, 2, 3, 4, 5, 6, 8], [0, 1, 2, 3, 4, 5, 6, 8], [7, 8], [0, 7, 8], [1, 7, 8], [0, 1, 7, 8], [2, 7, 8], [0, 2, 7, 8], [1, 2, 7, 8], [0, 1, 2, 7, 8], [3, 7, 8], [0, 3, 7, 8], [1, 3, 7, 8], [0, 1, 3, 7, 8], [2, 3, 7, 8], [0, 2, 3, 7, 8], [1, 2, 3, 7, 8], [0, 1, 2, 3, 7, 8], [4, 7, 8], [0, 4, 7, 8], [1, 4, 7, 8], [0, 1, 4, 7, 8], [2, 4, 7, 8], [0, 2, 4, 7, 8], [1, 2, 4, 7, 8], [0, 1, 2, 4, 7, 8], [3, 4, 7, 8], [0, 3, 4, 7, 8], [1, 3, 4, 7, 8], [0, 1, 3, 4, 7, 8], [2, 3, 4, 7, 8], [0, 2, 3, 4, 7, 8], [1, 2, 3, 4, 7, 8], [0, 1, 2, 3, 4, 7, 8], [5, 7, 8], [0, 5, 7, 8], [1, 5, 7, 8], [0, 1, 5, 7, 8], [2, 5, 7, 8], [0, 2, 5, 7, 8], [1, 2, 5, 7, 8], [0, 1, 2, 5, 7, 8], [3, 5, 7, 8], [0, 3, 5, 7, 8], [1, 3, 5, 7, 8], [0, 1, 3, 5, 7, 8], [2, 3, 5, 7, 8], [0, 2, 3, 5, 7, 8], [1, 2, 3, 5, 7, 8], [0, 1, 2, 3, 5, 7, 8], [4, 5, 7, 8], [0, 4, 5, 7, 8], [1, 4, 5, 7, 8], [0, 1, 4, 5, 7, 8], [2, 4, 5, 7, 8], [0, 2, 4, 5, 7, 8], [1, 2, 4, 5, 7, 8], [0, 1, 2, 4, 5, 7, 8], [3, 4, 5, 7, 8], [0, 3, 4, 5, 7, 8], [1, 3, 4, 5, 7, 8], [0, 1, 3, 4, 5, 7, 8], [2, 3, 4, 5, 7, 8], [0, 2, 3, 4, 5, 7, 8], [1, 2, 3, 4, 5, 7, 8], [0, 1, 2, 3, 4, 5, 7, 8], [6, 7, 8], [0, 6, 7, 8], [1, 6, 7, 8], [0, 1, 6, 7, 8], [2, 6, 7, 8], [0, 2, 6, 7, 8], [1, 2, 6, 7, 8], [0, 1, 2, 6, 7, 8], [3, 6, 7, 8], [0, 3, 6, 7, 8], [1, 3, 6, 7, 8], [0, 1, 3, 6, 7, 8], [2, 3, 6, 7, 8], [0, 2, 3, 6, 7, 8], [1, 2, 3, 6, 7, 8], [0, 1, 2, 3, 6, 7, 8], [4, 6, 7, 8], [0, 4, 6, 7, 8], [1, 4, 6, 7, 8], [0, 1, 4, 6, 7, 8], [2, 4, 6, 7, 8], [0, 2, 4, 6, 7, 8], [1, 2, 4, 6, 7, 8], [0, 1, 2, 4, 6, 7, 8], [3, 4, 6, 7, 8], [0, 3, 4, 6, 7, 8], [1, 3, 4, 6, 7, 8], [0, 1, 3, 4, 6, 7, 8], [2, 3, 4, 6, 7, 8], [0, 2, 3, 4, 6, 7, 8], [1, 2, 3, 4, 6, 7, 8], [0, 1, 2, 3, 4, 6, 7, 8], [5, 6, 7, 8], [0, 5, 6, 7, 8], [1, 5, 6, 7, 8], [0, 1, 5, 6, 7, 8], [2, 5, 6, 7, 8], [0, 2, 5, 6, 7, 8], [1, 2, 5, 6, 7, 8], [0, 1, 2, 5, 6, 7, 8], [3, 5, 6, 7, 8], [0, 3, 5, 6, 7, 8], [1, 3, 5, 6, 7, 8], [0, 1, 3, 5, 6, 7, 8], [2, 3, 5, 6, 7, 8], [0, 2, 3, 5, 6, 7, 8], [1, 2, 3, 5, 6, 7, 8], [0, 1, 2, 3, 5, 6, 7, 8], [4, 5, 6, 7, 8], [0, 4, 5, 6, 7, 8], [1, 4, 5, 6, 7, 8], [0, 1, 4, 5, 6, 7, 8], [2, 4, 5, 6, 7, 8], [0, 2, 4, 5, 6, 7, 8], [1, 2, 4, 5, 6, 7, 8], [0, 1, 2, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8], [0, 3, 4, 5, 6, 7, 8], [1, 3, 4, 5, 6, 7, 8], [0, 1, 3, 4, 5, 6, 7, 8], [2, 3, 4, 5, 6, 7, 8], [0, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [9], [0, 9], [1, 9], [0, 1, 9], [2, 9], [0, 2, 9], [1, 2, 9], [0, 1, 2, 9], [3, 9], [0, 3, 9], [1, 3, 9], [0, 1, 3, 9], [2, 3, 9], [0, 2, 3, 9], [1, 2, 3, 9], [0, 1, 2, 3, 9], [4, 9], [0, 4, 9], [1, 4, 9], [0, 1, 4, 9], [2, 4, 9], [0, 2, 4, 9], [1, 2, 4, 9], [0, 1, 2, 4, 9], [3, 4, 9], [0, 3, 4, 9], [1, 3, 4, 9], [0, 1, 3, 4, 9], [2, 3, 4, 9], [0, 2, 3, 4, 9], [1, 2, 3, 4, 9], [0, 1, 2, 3, 4, 9], [5, 9], [0, 5, 9], [1, 5, 9], [0, 1, 5, 9], [2, 5, 9], [0, 2, 5, 9], [1, 2, 5, 9], [0, 1, 2, 5, 9], [3, 5, 9], [0, 3, 5, 9], [1, 3, 5, 9], [0, 1, 3, 5, 9], [2, 3, 5, 9], [0, 2, 3, 5, 9], [1, 2, 3, 5, 9], [0, 1, 2, 3, 5, 9], [4, 5, 9], [0, 4, 5, 9], [1, 4, 5, 9], [0, 1, 4, 5, 9], [2, 4, 5, 9], [0, 2, 4, 5, 9], [1, 2, 4, 5, 9], [0, 1, 2, 4, 5, 9], [3, 4, 5, 9], [0, 3, 4, 5, 9], [1, 3, 4, 5, 9], [0, 1, 3, 4, 5, 9], [2, 3, 4, 5, 9], [0, 2, 3, 4, 5, 9], [1, 2, 3, 4, 5, 9], [0, 1, 2, 3, 4, 5, 9], [6, 9], [0, 6, 9], [1, 6, 9], [0, 1, 6, 9], [2, 6, 9], [0, 2, 6, 9], [1, 2, 6, 9], [0, 1, 2, 6, 9], [3, 6, 9], [0, 3, 6, 9], [1, 3, 6, 9], [0, 1, 3, 6, 9], [2, 3, 6, 9], [0, 2, 3, 6, 9], [1, 2, 3, 6, 9], [0, 1, 2, 3, 6, 9], [4, 6, 9], [0, 4, 6, 9], [1, 4, 6, 9], [0, 1, 4, 6, 9], [2, 4, 6, 9], [0, 2, 4, 6, 9], [1, 2, 4, 6, 9], [0, 1, 2, 4, 6, 9], [3, 4, 6, 9], [0, 3, 4, 6, 9], [1, 3, 4, 6, 9], [0, 1, 3, 4, 6, 9], [2, 3, 4, 6, 9], [0, 2, 3, 4, 6, 9], [1, 2, 3, 4, 6, 9], [0, 1, 2, 3, 4, 6, 9], [5, 6, 9], [0, 5, 6, 9], [1, 5, 6, 9], [0, 1, 5, 6, 9], [2, 5, 6, 9], [0, 2, 5, 6, 9], [1, 2, 5, 6, 9], [0, 1, 2, 5, 6, 9], [3, 5, 6, 9], [0, 3, 5, 6, 9], [1, 3, 5, 6, 9], [0, 1, 3, 5, 6, 9], [2, 3, 5, 6, 9], [0, 2, 3, 5, 6, 9], [1, 2, 3, 5, 6, 9], [0, 1, 2, 3, 5, 6, 9], [4, 5, 6, 9], [0, 4, 5, 6, 9], [1, 4, 5, 6, 9], [0, 1, 4, 5, 6, 9], [2, 4, 5, 6, 9], [0, 2, 4, 5, 6, 9], [1, 2, 4, 5, 6, 9], [0, 1, 2, 4, 5, 6, 9], [3, 4, 5, 6, 9], [0, 3, 4, 5, 6, 9], [1, 3, 4, 5, 6, 9], [0, 1, 3, 4, 5, 6, 9], [2, 3, 4, 5, 6, 9], [0, 2, 3, 4, 5, 6, 9], [1, 2, 3, 4, 5, 6, 9], [0, 1, 2, 3, 4, 5, 6, 9], [7, 9], [0, 7, 9], [1, 7, 9], [0, 1, 7, 9], [2, 7, 9], [0, 2, 7, 9], [1, 2, 7, 9], [0, 1, 2, 7, 9], [3, 7, 9], [0, 3, 7, 9], [1, 3, 7, 9], [0, 1, 3, 7, 9], [2, 3, 7, 9], [0, 2, 3, 7, 9], [1, 2, 3, 7, 9], [0, 1, 2, 3, 7, 9], [4, 7, 9], [0, 4, 7, 9], [1, 4, 7, 9], [0, 1, 4, 7, 9], [2, 4, 7, 9], [0, 2, 4, 7, 9], [1, 2, 4, 7, 9], [0, 1, 2, 4, 7, 9], [3, 4, 7, 9], [0, 3, 4, 7, 9], [1, 3, 4, 7, 9], [0, 1, 3, 4, 7, 9], [2, 3, 4, 7, 9], [0, 2, 3, 4, 7, 9], [1, 2, 3, 4, 7, 9], [0, 1, 2, 3, 4, 7, 9], [5, 7, 9], [0, 5, 7, 9], [1, 5, 7, 9], [0, 1, 5, 7, 9], [2, 5, 7, 9], [0, 2, 5, 7, 9], [1, 2, 5, 7, 9], [0, 1, 2, 5, 7, 9], [3, 5, 7, 9], [0, 3, 5, 7, 9], [1, 3, 5, 7, 9], [0, 1, 3, 5, 7, 9], [2, 3, 5, 7, 9], [0, 2, 3, 5, 7, 9], [1, 2, 3, 5, 7, 9], [0, 1, 2, 3, 5, 7, 9], [4, 5, 7, 9], [0, 4, 5, 7, 9], [1, 4, 5, 7, 9], [0, 1, 4, 5, 7, 9], [2, 4, 5, 7, 9], [0, 2, 4, 5, 7, 9], [1, 2, 4, 5, 7, 9], [0, 1, 2, 4, 5, 7, 9], [3, 4, 5, 7, 9], [0, 3, 4, 5, 7, 9], [1, 3, 4, 5, 7, 9], [0, 1, 3, 4, 5, 7, 9], [2, 3, 4, 5, 7, 9], [0, 2, 3, 4, 5, 7, 9], [1, 2, 3, 4, 5, 7, 9], [0, 1, 2, 3, 4, 5, 7, 9], [6, 7, 9], [0, 6, 7, 9], [1, 6, 7, 9], [0, 1, 6, 7, 9], [2, 6, 7, 9], [0, 2, 6, 7, 9], [1, 2, 6, 7, 9], [0, 1, 2, 6, 7, 9], [3, 6, 7, 9], [0, 3, 6, 7, 9], [1, 3, 6, 7, 9], [0, 1, 3, 6, 7, 9], [2, 3, 6, 7, 9], [0, 2, 3, 6, 7, 9], [1, 2, 3, 6, 7, 9], [0, 1, 2, 3, 6, 7, 9], [4, 6, 7, 9], [0, 4, 6, 7, 9], [1, 4, 6, 7, 9], [0, 1, 4, 6, 7, 9], [2, 4, 6, 7, 9], [0, 2, 4, 6, 7, 9], [1, 2, 4, 6, 7, 9], [0, 1, 2, 4, 6, 7, 9], [3, 4, 6, 7, 9], [0, 3, 4, 6, 7, 9], [1, 3, 4, 6, 7, 9], [0, 1, 3, 4, 6, 7, 9], [2, 3, 4, 6, 7, 9], [0, 2, 3, 4, 6, 7, 9], [1, 2, 3, 4, 6, 7, 9], [0, 1, 2, 3, 4, 6, 7, 9], [5, 6, 7, 9], [0, 5, 6, 7, 9], [1, 5, 6, 7, 9], [0, 1, 5, 6, 7, 9], [2, 5, 6, 7, 9], [0, 2, 5, 6, 7, 9], [1, 2, 5, 6, 7, 9], [0, 1, 2, 5, 6, 7, 9], [3, 5, 6, 7, 9], [0, 3, 5, 6, 7, 9], [1, 3, 5, 6, 7, 9], [0, 1, 3, 5, 6, 7, 9], [2, 3, 5, 6, 7, 9], [0, 2, 3, 5, 6, 7, 9], [1, 2, 3, 5, 6, 7, 9], [0, 1, 2, 3, 5, 6, 7, 9], [4, 5, 6, 7, 9], [0, 4, 5, 6, 7, 9], [1, 4, 5, 6, 7, 9], [0, 1, 4, 5, 6, 7, 9], [2, 4, 5, 6, 7, 9], [0, 2, 4, 5, 6, 7, 9], [1, 2, 4, 5, 6, 7, 9], [0, 1, 2, 4, 5, 6, 7, 9], [3, 4, 5, 6, 7, 9], [0, 3, 4, 5, 6, 7, 9], [1, 3, 4, 5, 6, 7, 9], [0, 1, 3, 4, 5, 6, 7, 9], [2, 3, 4, 5, 6, 7, 9], [0, 2, 3, 4, 5, 6, 7, 9], [1, 2, 3, 4, 5, 6, 7, 9], [0, 1, 2, 3, 4, 5, 6, 7, 9], [8, 9], [0, 8, 9], [1, 8, 9], [0, 1, 8, 9], [2, 8, 9], [0, 2, 8, 9], [1, 2, 8, 9], [0, 1, 2, 8, 9], [3, 8, 9], [0, 3, 8, 9], [1, 3, 8, 9], [0, 1, 3, 8, 9], [2, 3, 8, 9], [0, 2, 3, 8, 9], [1, 2, 3, 8, 9], [0, 1, 2, 3, 8, 9], [4, 8, 9], [0, 4, 8, 9], [1, 4, 8, 9], [0, 1, 4, 8, 9], [2, 4, 8, 9], [0, 2, 4, 8, 9], [1, 2, 4, 8, 9], [0, 1, 2, 4, 8, 9], [3, 4, 8, 9], [0, 3, 4, 8, 9], [1, 3, 4, 8, 9], [0, 1, 3, 4, 8, 9], [2, 3, 4, 8, 9], [0, 2, 3, 4, 8, 9], [1, 2, 3, 4, 8, 9], [0, 1, 2, 3, 4, 8, 9], [5, 8, 9], [0, 5, 8, 9], [1, 5, 8, 9], [0, 1, 5, 8, 9], [2, 5, 8, 9], [0, 2, 5, 8, 9], [1, 2, 5, 8, 9], [0, 1, 2, 5, 8, 9], [3, 5, 8, 9], [0, 3, 5, 8, 9], [1, 3, 5, 8, 9], [0, 1, 3, 5, 8, 9], [2, 3, 5, 8, 9], [0, 2, 3, 5, 8, 9], [1, 2, 3, 5, 8, 9], [0, 1, 2, 3, 5, 8, 9], [4, 5, 8, 9], [0, 4, 5, 8, 9], [1, 4, 5, 8, 9], [0, 1, 4, 5, 8, 9], [2, 4, 5, 8, 9], [0, 2, 4, 5, 8, 9], [1, 2, 4, 5, 8, 9], [0, 1, 2, 4, 5, 8, 9], [3, 4, 5, 8, 9], [0, 3, 4, 5, 8, 9], [1, 3, 4, 5, 8, 9], [0, 1, 3, 4, 5, 8, 9], [2, 3, 4, 5, 8, 9], [0, 2, 3, 4, 5, 8, 9], [1, 2, 3, 4, 5, 8, 9], [0, 1, 2, 3, 4, 5, 8, 9], [6, 8, 9], [0, 6, 8, 9], [1, 6, 8, 9], [0, 1, 6, 8, 9], [2, 6, 8, 9], [0, 2, 6, 8, 9], [1, 2, 6, 8, 9], [0, 1, 2, 6, 8, 9], [3, 6, 8, 9], [0, 3, 6, 8, 9], [1, 3, 6, 8, 9], [0, 1, 3, 6, 8, 9], [2, 3, 6, 8, 9], [0, 2, 3, 6, 8, 9], [1, 2, 3, 6, 8, 9], [0, 1, 2, 3, 6, 8, 9], [4, 6, 8, 9], [0, 4, 6, 8, 9], [1, 4, 6, 8, 9], [0, 1, 4, 6, 8, 9], [2, 4, 6, 8, 9], [0, 2, 4, 6, 8, 9], [1, 2, 4, 6, 8, 9], [0, 1, 2, 4, 6, 8, 9], [3, 4, 6, 8, 9], [0, 3, 4, 6, 8, 9], [1, 3, 4, 6, 8, 9], [0, 1, 3, 4, 6, 8, 9], [2, 3, 4, 6, 8, 9], [0, 2, 3, 4, 6, 8, 9], [1, 2, 3, 4, 6, 8, 9], [0, 1, 2, 3, 4, 6, 8, 9], [5, 6, 8, 9], [0, 5, 6, 8, 9], [1, 5, 6, 8, 9], [0, 1, 5, 6, 8, 9], [2, 5, 6, 8, 9], [0, 2, 5, 6, 8, 9], [1, 2, 5, 6, 8, 9], [0, 1, 2, 5, 6, 8, 9], [3, 5, 6, 8, 9], [0, 3, 5, 6, 8, 9], [1, 3, 5, 6, 8, 9], [0, 1, 3, 5, 6, 8, 9], [2, 3, 5, 6, 8, 9], [0, 2, 3, 5, 6, 8, 9], [1, 2, 3, 5, 6, 8, 9], [0, 1, 2, 3, 5, 6, 8, 9], [4, 5, 6, 8, 9], [0, 4, 5, 6, 8, 9], [1, 4, 5, 6, 8, 9], [0, 1, 4, 5, 6, 8, 9], [2, 4, 5, 6, 8, 9], [0, 2, 4, 5, 6, 8, 9], [1, 2, 4, 5, 6, 8, 9], [0, 1, 2, 4, 5, 6, 8, 9], [3, 4, 5, 6, 8, 9], [0, 3, 4, 5, 6, 8, 9], [1, 3, 4, 5, 6, 8, 9], [0, 1, 3, 4, 5, 6, 8, 9], [2, 3, 4, 5, 6, 8, 9], [0, 2, 3, 4, 5, 6, 8, 9], [1, 2, 3, 4, 5, 6, 8, 9], [0, 1, 2, 3, 4, 5, 6, 8, 9], [7, 8, 9], [0, 7, 8, 9], [1, 7, 8, 9], [0, 1, 7, 8, 9], [2, 7, 8, 9], [0, 2, 7, 8, 9], [1, 2, 7, 8, 9], [0, 1, 2, 7, 8, 9], [3, 7, 8, 9], [0, 3, 7, 8, 9], [1, 3, 7, 8, 9], [0, 1, 3, 7, 8, 9], [2, 3, 7, 8, 9], [0, 2, 3, 7, 8, 9], [1, 2, 3, 7, 8, 9], [0, 1, 2, 3, 7, 8, 9], [4, 7, 8, 9], [0, 4, 7, 8, 9], [1, 4, 7, 8, 9], [0, 1, 4, 7, 8, 9], [2, 4, 7, 8, 9], [0, 2, 4, 7, 8, 9], [1, 2, 4, 7, 8, 9], [0, 1, 2, 4, 7, 8, 9], [3, 4, 7, 8, 9], [0, 3, 4, 7, 8, 9], [1, 3, 4, 7, 8, 9], [0, 1, 3, 4, 7, 8, 9], [2, 3, 4, 7, 8, 9], [0, 2, 3, 4, 7, 8, 9], [1, 2, 3, 4, 7, 8, 9], [0, 1, 2, 3, 4, 7, 8, 9], [5, 7, 8, 9], [0, 5, 7, 8, 9], [1, 5, 7, 8, 9], [0, 1, 5, 7, 8, 9], [2, 5, 7, 8, 9], [0, 2, 5, 7, 8, 9], [1, 2, 5, 7, 8, 9], [0, 1, 2, 5, 7, 8, 9], [3, 5, 7, 8, 9], [0, 3, 5, 7, 8, 9], [1, 3, 5, 7, 8, 9], [0, 1, 3, 5, 7, 8, 9], [2, 3, 5, 7, 8, 9], [0, 2, 3, 5, 7, 8, 9], [1, 2, 3, 5, 7, 8, 9], [0, 1, 2, 3, 5, 7, 8, 9], [4, 5, 7, 8, 9], [0, 4, 5, 7, 8, 9], [1, 4, 5, 7, 8, 9], [0, 1, 4, 5, 7, 8, 9], [2, 4, 5, 7, 8, 9], [0, 2, 4, 5, 7, 8, 9], [1, 2, 4, 5, 7, 8, 9], [0, 1, 2, 4, 5, 7, 8, 9], [3, 4, 5, 7, 8, 9], [0, 3, 4, 5, 7, 8, 9], [1, 3, 4, 5, 7, 8, 9], [0, 1, 3, 4, 5, 7, 8, 9], [2, 3, 4, 5, 7, 8, 9], [0, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9], [0, 1, 2, 3, 4, 5, 7, 8, 9], [6, 7, 8, 9], [0, 6, 7, 8, 9], [1, 6, 7, 8, 9], [0, 1, 6, 7, 8, 9], [2, 6, 7, 8, 9], [0, 2, 6, 7, 8, 9], [1, 2, 6, 7, 8, 9], [0, 1, 2, 6, 7, 8, 9], [3, 6, 7, 8, 9], [0, 3, 6, 7, 8, 9], [1, 3, 6, 7, 8, 9], [0, 1, 3, 6, 7, 8, 9], [2, 3, 6, 7, 8, 9], [0, 2, 3, 6, 7, 8, 9], [1, 2, 3, 6, 7, 8, 9], [0, 1, 2, 3, 6, 7, 8, 9], [4, 6, 7, 8, 9], [0, 4, 6, 7, 8, 9], [1, 4, 6, 7, 8, 9], [0, 1, 4, 6, 7, 8, 9], [2, 4, 6, 7, 8, 9], [0, 2, 4, 6, 7, 8, 9], [1, 2, 4, 6, 7, 8, 9], [0, 1, 2, 4, 6, 7, 8, 9], [3, 4, 6, 7, 8, 9], [0, 3, 4, 6, 7, 8, 9], [1, 3, 4, 6, 7, 8, 9], [0, 1, 3, 4, 6, 7, 8, 9], [2, 3, 4, 6, 7, 8, 9], [0, 2, 3, 4, 6, 7, 8, 9], [1, 2, 3, 4, 6, 7, 8, 9], [0, 1, 2, 3, 4, 6, 7, 8, 9], [5, 6, 7, 8, 9], [0, 5, 6, 7, 8, 9], [1, 5, 6, 7, 8, 9], [0, 1, 5, 6, 7, 8, 9], [2, 5, 6, 7, 8, 9], [0, 2, 5, 6, 7, 8, 9], [1, 2, 5, 6, 7, 8, 9], [0, 1, 2, 5, 6, 7, 8, 9], [3, 5, 6, 7, 8, 9], [0, 3, 5, 6, 7, 8, 9], [1, 3, 5, 6, 7, 8, 9], [0, 1, 3, 5, 6, 7, 8, 9], [2, 3, 5, 6, 7, 8, 9], [0, 2, 3, 5, 6, 7, 8, 9], [1, 2, 3, 5, 6, 7, 8, 9], [0, 1, 2, 3, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9], [0, 4, 5, 6, 7, 8, 9], [1, 4, 5, 6, 7, 8, 9], [0, 1, 4, 5, 6, 7, 8, 9], [2, 4, 5, 6, 7, 8, 9], [0, 2, 4, 5, 6, 7, 8, 9], [1, 2, 4, 5, 6, 7, 8, 9], [0, 1, 2, 4, 5, 6, 7, 8, 9], [3, 4, 5, 6, 7, 8, 9], [0, 3, 4, 5, 6, 7, 8, 9], [1, 3, 4, 5, 6, 7, 8, 9], [0, 1, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9], [0, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
print(output, answer, answer == output)
