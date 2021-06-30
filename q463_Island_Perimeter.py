from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        h,w = len(grid),len(grid[0])
        for i in range(h):
            for j in range(w):
                if grid[i][j]==1:
                    perimeter+=4
                    if 0<i and grid[i-1][j]==1:
                        perimeter-=1
                    if i<h-1 and grid[i+1][j]==1:
                        perimeter-=1
                    if 0<j and grid[i][j-1]==1:
                        perimeter-=1
                    if j<w-1 and grid[i][j+1]==1:
                        perimeter-=1
        return perimeter

sol = Solution()


# input
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# output
output = sol.islandPerimeter(grid)
# answer
answer = 16
print(output, answer, answer == output)

# input
grid = [[1]]
# output
output = sol.islandPerimeter(grid)
# answer
answer = 4
print(output, answer, answer == output)

# input
grid = [[1,0]]
# output
output = sol.islandPerimeter(grid)
# answer
answer = 4
print(output, answer, answer == output)
