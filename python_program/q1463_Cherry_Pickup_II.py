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
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        level_grid = np.zeros((m,m))
        level_grid[0,m-1]=grid[0][0]+grid[0][m-1]+1
        for k in range(1,n):
            next_level_grid = np.zeros((m,m))
            for i in range(m):
                for j in range(m):
                    if i!=j:
                        max_list = [0]
                        for ii in [-1,0,1]:
                            for jj in [-1,0,1]:
                                if 0<=i+ii<=m-1 and 0<=j+jj<=m-1 and i+ii!=j+jj:
                                    if level_grid[i+ii,j+jj]:
                                        max_list.append(level_grid[i+ii,j+jj]+grid[k][i]+grid[k][j])
                        next_level_grid[i,j] = max(max_list)
                        
            level_grid = next_level_grid
        return int(level_grid.max())-1

sol = Solution()

# input
grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]

# output
output = sol.cherryPickup(grid)
# answer
answer = 24

print(output, answer, answer == output)

# input
grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]

# output
output = sol.cherryPickup(grid)
# answer
answer = 28

print(output, answer, answer == output)

# input
grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]

# output
output = sol.cherryPickup(grid)
# answer
answer = 22

print(output, answer, answer == output)

# input
grid = [[1,1],[1,1]]

# output
output = sol.cherryPickup(grid)
# answer
answer = 4

print(output, answer, answer == output)

# input
grid = [[0,0,10,2,8,4,0],[7,9,3,5,4,8,3],[6,9,8,3,5,6,0],[0,4,1,1,9,3,7],[5,6,9,8,8,10,10],[9,2,9,7,4,8,3],[1,6,1,2,0,9,9]]

# output
output = sol.cherryPickup(grid)
# answer
answer = 22

print(output, answer, answer == output)

# input
grid = [[1,1],[1,1]]

# output
output = sol.cherryPickup(grid)
# answer
answer = 4

print(output, answer, answer == output)

# input
grid = [[0,0,10,2,8,4,0],[7,9,3,5,4,8,3],[6,9,8,3,5,6,0],[0,4,1,1,9,3,7],[5,6,9,8,8,10,10],[9,2,9,7,4,8,3],[1,6,1,2,0,9,9]]

# output
output = sol.cherryPickup(grid)
# answer
answer = 96

print(output, answer, answer == output)
