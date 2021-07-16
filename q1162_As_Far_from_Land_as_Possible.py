from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count_water = 0
        count_land  = 0
        land_covered = []
        visited_water = set()
        for i in range(n):
            for j in range(n):
                cell = grid[i][j]
                if cell == 0:
                    count_water+=1
                else:
                    count_land+=1
                    land_covered.append((i,j))
        if count_water == 0 or count_land == 0:
            return -1
                
        max_distance = 0
        while land_covered:
            new_list = []
            return_max_distance = True
            for x,y in land_covered:
                for delta_x,delta_y in ((0,1),(0,-1),(1,0),(-1,0)):
                    new_x,new_y = x+delta_x,y+delta_y
                    
                    if 0<=new_x<n and 0<=new_y<n and not grid[new_x][new_y] and (new_x,new_y) not in visited_water:
                        new_list.append((new_x,new_y))
                        visited_water.add((new_x,new_y))
                        return_max_distance = False
            land_covered = new_list
            if return_max_distance:
                break
            max_distance += 1

        return max_distance

sol = Solution()


# input
grid = [[1,0,1],[0,0,0],[1,0,1]]
# output
output = sol.maxDistance(grid)
# answer
answer = 2
print(output, answer, answer == output)

# input
grid = [[1,0,0],[0,0,0],[0,0,0]]
# output
output = sol.maxDistance(grid)
# answer
answer = 4
print(output, answer, answer == output)

# input
grid = [[1,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
# output
output = sol.maxDistance(grid)
# answer
answer = 3
print(output, answer, answer == output)
