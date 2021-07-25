from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        self.grid = grid
        m,n = len(grid),len(grid[0])
        self.m,self.n = m,n
        return [self.exit_path(0,i) for i in range(n)]

    def findBall_1(self, grid: List[List[int]]) -> List[int]:
        self.grid = grid
        m,n = len(grid),len(grid[0])
        self.m,self.n = m,n
        return_list = [0]*n
        for i in range(n):
            return_list[i] = self.exit_path(0,i)
        return return_list

    def exit_path(self,row,col):
        if row == self.m:
            return col
        if (col == 0 and self.grid[row][col]==-1) or (col ==self.n-1 and self.grid[row][col]==1):
            return -1
        if col<self.n-1 and (self.grid[row][col]==1 and self.grid[row][col+1]==1):
            return self.exit_path(row+1,col+1)
        if 0<col and (self.grid[row][col]==-1 and self.grid[row][col-1]==-1):
            return self.exit_path(row+1,col-1)
        return -1
        

sol = Solution()

# input
grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]

# output
output = sol.findBall(grid)
# answer
answer = [1,-1,-1,-1,-1]
print(output, answer, answer == output)

# input
grid = [[-1]]

# output
output = sol.findBall(grid)
# answer
answer = [-1]
print(output, answer, answer == output)

# input
grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]

# output
output = sol.findBall(grid)
# answer
answer = [0,1,2,3,4,-1]
print(output, answer, answer == output)
