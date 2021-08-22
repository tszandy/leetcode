from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        total_area = 0
        n = len(grid)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    total_area += grid[i][j]*6-(grid[i][j]-1)*2
                    if i+1<n:
                        total_area-= min(grid[i][j],grid[i+1][j])*2
                    if j+1<n:
                        total_area-= min(grid[i][j],grid[i][j+1])*2
        return total_area

sol = Solution()


# input
grid = [[2]]
# output
output = sol.surfaceArea(grid)
# answer
answer = 10
print(output, answer, answer == output)

# input
grid = [[1,2],[3,4]]
# output
output = sol.surfaceArea(grid)
# answer
answer = 34
print(output, answer, answer == output)

# input
grid = [[1,0],[0,2]]
# output
output = sol.surfaceArea(grid)
# answer
answer = 16
print(output, answer, answer == output)

# input
grid = [[1,1,1],[1,0,1],[1,1,1]]
# output
output = sol.surfaceArea(grid)
# answer
answer = 32
print(output, answer, answer == output)

# input
grid = [[2,2,2],[2,1,2],[2,2,2]]
# output
output = sol.surfaceArea(grid)
# answer
answer = 46
print(output, answer, answer == output)
