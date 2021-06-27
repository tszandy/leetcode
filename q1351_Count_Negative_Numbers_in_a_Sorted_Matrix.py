from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid[::-1]:
            if row[-1]>=0:
                return count
            for num in row[::-1]:
                if num <0:
                    count +=1
        return count

sol = Solution()


# input
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# output
output = sol.countNegatives(grid)
# answer
answer = 8
print(output, answer, answer == output)

# input
grid = [[3,2],[1,0]]
# output
output = sol.countNegatives(grid)
# answer
answer = 0
print(output, answer, answer == output)

# input
grid = [[1,-1],[-1,-1]]
# output
output = sol.countNegatives(grid)
# answer
answer = 3
print(output, answer, answer == output)
