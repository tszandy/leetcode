from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        left = values[0]
        left_index = 0
        max_score = 0
        n = len(values)
        for i in range(1,n):
            max_score = max(max_score, left + values[i] + left_index-i)
            if left + left_index<values[i]+i:
                left = values[i]
                left_index = i
        return max_score

sol = Solution()


# input
values = [8,1,5,2,6]
# output
output = sol.maxScoreSightseeingPair(values)
# answer
answer = 11
print(output, answer, answer == output)

# input
values = [1,2]
# output
output = sol.maxScoreSightseeingPair(values)
# answer
answer = 2
print(output, answer, answer == output)

# input
values = [1,2,8,1,2,3,4,1,2,1,3,4,5,1,2]
# output
output = sol.maxScoreSightseeingPair(values)
# answer
answer = 9
print(output, answer, answer == output)
