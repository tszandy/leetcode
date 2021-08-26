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
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid),len(grid[0])
        sum_set = set()
        rhombus_radiu = (min(m,n)-1)//2
        for i in range(m):
            for j in range(n):
                sum_set.add(grid[i][j])
                for r in range(1,rhombus_radiu+1):
                    if i+r<=m-1 and i-r>=0 and j+r<=n-1 and j-r>=0:
                        up = (i,j-r)
                        down = (i,j+r)
                        left = (i-r,j)
                        right = (i+r,j)
                        rho_sum = 0
                        for a,b in zip(range(up[0],right[0]),range(up[1],right[1])):
                            rho_sum+=grid[a][b]
                        for a,b in zip(range(right[0],down[0],-1),range(right[1],down[1])):
                            rho_sum+=grid[a][b]
                        for a,b in zip(range(down[0],left[0],-1),range(down[1],left[1],-1)):
                            rho_sum+=grid[a][b]
                        for a,b in zip(range(left[0],up[0]),range(left[1],up[1],-1)):
                            rho_sum+=grid[a][b]
                        sum_set.add(rho_sum)
                    else:
                        break
        return sorted(list(sum_set),key = lambda x:-x)[:3]

sol = Solution()

# input
grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]

# output
output = sol.getBiggestThree(grid)
# answer
answer = [228,216,211]

print(output, answer, answer == output)

# input
grid = [[1,2,3],[4,5,6],[7,8,9]]

# output
output = sol.getBiggestThree(grid)
# answer
answer = [20,9,8]

print(output, answer, answer == output)

# input
grid = [[7,7,7]]

# output
output = sol.getBiggestThree(grid)
# answer
answer = [7]

print(output, answer, answer == output)
