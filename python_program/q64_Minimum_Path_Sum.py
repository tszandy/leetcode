from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        m,n = len(grid),len(grid[0])
        dp[(0,0)] = grid[0][0]
        for i in range(1,m):
            dp[(i,0)]=grid[i][0]+dp[(i-1,0)]
        for i in range(1,n):
            dp[(0,i)]=grid[0][i]+dp[(0,i-1)]
        for i in range(1,m):
            for j in range(1,n):
                dp[(i,j)] = min(dp[(i-1,j)]+grid[i][j],dp[(i,j-1)]+grid[i][j])
        return dp[(m-1,n-1)]


#BFS not BFS problem wrong answer
    def minPathSum_1(self, grid: List[List[int]]) -> int:
        hq = []
        m,n = len(grid),len(grid[0])
        heappush(hq, (grid[0][0],(0,0)))
        record_visited = set()
        
        while hq:
            cost, (x,y) = heappop(hq)
            if x == m-1 and y == n-1:
                return cost
            record_visited.add((x,y))
            if 0<x and (x-1,y) not in record_visited:
                heappush(hq,(cost+grid[x-1][y],(x-1,y)))
            if x<m-1 and (x+1,y) not in record_visited:
                heappush(hq,(cost+grid[x+1][y],(x+1,y)))
            if 0<y and (x,y-1) not in record_visited:
                heappush(hq,(cost+grid[x][y-1],(x,y-1)))
            if y<n-1 and (x,y+1) not in record_visited:
                heappush(hq,(cost+grid[x][y+1],(x,y+1)))


sol = Solution()


# input
grid = [[1,3,1],[1,5,1],[4,2,1]]
# output
output = sol.minPathSum(grid)
# answer
answer = 7
print(output, answer, answer == output)

# input
grid = [[1,2,3],[4,5,6]]
# output
output = sol.minPathSum(grid)
# answer
answer = 12
print(output, answer, answer == output)

# input
grid = [[4,5,2,1,5,6,7,0,1,3],[6,8,2,9,1,5,5,1,5,1],[6,4,6,8,0,7,1,7,3,5],[6,9,2,8,0,9,6,0,1,8]]
# output
output = sol.minPathSum(grid)
# answer
answer = 41
print(output, answer, answer == output)

# input
grid = [[1,5,1,1,1,1],[1,5,1,5,5,1],[1,5,1,1,5,1],[1,5,5,1,5,1],[1,1,1,1,5,1]]
# output
output = sol.minPathSum(grid)
# answer
answer = 14
print(output, answer, answer == output)

# input
grid = [[5,4,2,9,6,0,3,5,1,4,9,8,4,9,7,5,1],[3,4,9,2,9,9,0,9,7,9,4,7,8,4,4,5,8],[6,1,8,9,8,0,3,7,0,9,8,7,4,9,2,0,1],[4,0,0,5,1,7,4,7,6,4,1,0,1,0,6,2,8],[7,2,0,2,9,3,4,7,0,8,9,5,9,0,1,1,0],[8,2,9,4,9,7,9,3,7,0,3,6,5,3,5,9,6],[8,9,9,2,6,1,2,5,8,3,7,0,4,9,8,8,8],[5,8,5,4,1,5,6,6,3,3,1,8,3,9,6,4,8],[0,2,2,3,0,2,6,7,2,3,7,3,1,5,8,1,3],[4,4,0,2,0,3,8,4,1,3,3,0,7,4,2,9,8],[5,9,0,4,7,5,7,6,0,8,3,0,0,6,6,6,8],[0,7,1,8,3,5,1,8,7,0,2,9,2,2,7,1,5],[1,0,0,0,6,2,0,0,2,2,8,0,9,7,0,8,0],[1,1,7,2,9,6,5,4,8,7,8,5,0,3,8,1,5],[8,9,7,8,1,1,3,0,1,2,9,4,0,1,5,3,1],[9,2,7,4,8,7,3,9,2,4,2,2,7,8,2,6,7],[3,8,1,6,0,4,8,9,8,0,2,5,3,5,5,7,5],[1,8,2,5,7,7,1,9,9,8,9,2,4,9,5,4,0],[3,4,4,1,5,3,3,8,8,6,3,5,3,8,7,1,3]]
# output
output = sol.minPathSum(grid)
# answer
answer = 82
print(output, answer, answer == output)
