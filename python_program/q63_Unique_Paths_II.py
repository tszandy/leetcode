from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        grid_size = (m,n)
        store_path = {}
        
        def unique_path(m,n):
            if (m,n) in store_path:
                return store_path[(m,n)]

            if obstacleGrid[m][n]==1:
                store_path[(m,n)] = 0
                return store_path[(m,n)]
            
            if m == grid_size[0]-1 and n == grid_size[1]-1:
                store_path[(m,n)] = 1
                return store_path[(m,n)]
                
            if m == grid_size[0]-1:
                store_path[(m,n)] = unique_path(m,n+1)
                return store_path[(m,n)]

            if n == grid_size[1]-1:
                store_path[(m,n)] = unique_path(m+1,n)
                return store_path[(m,n)]
                        
            if (m,n) in store_path:
                return store_path[(m,n)]
            down = unique_path(m+1,n)
            right = unique_path(m,n+1)
            store_path[(m,n)] = down+right
            
            return store_path[(m,n)]

        unique_path(0,0)

        return store_path[(0,0)]

sol = Solution()


# input
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# output
output = sol.uniquePathsWithObstacles(obstacleGrid)
# answer
answer = 2
print(output, answer, answer == output)

# input
obstacleGrid = [[1]]
# output
output = sol.uniquePathsWithObstacles(obstacleGrid)
# answer
answer = 0
print(output, answer, answer == output)

# input
obstacleGrid = [[0]]
# output
output = sol.uniquePathsWithObstacles(obstacleGrid)
# answer
	answer = 1
print(output, answer, answer == output)

# input
obstacleGrid = [[0,1],[0,0]]
# output
output = sol.uniquePathsWithObstacles(obstacleGrid)
# answer
answer = 1
print(output, answer, answer == output)

# input
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0],[1,0,0],[0,1,0]]
# output
output = sol.uniquePathsWithObstacles(obstacleGrid)
# answer
answer = 3
print(output, answer, answer == output)

# input
obstacleGrid = [[0,0,0,0],[0,1,0,0],[0,0,0,0],[1,0,0,0],[0,1,0,0]]
# output
output = sol.uniquePathsWithObstacles(obstacleGrid)
# answer
answer = 10
print(output, answer, answer == output)
