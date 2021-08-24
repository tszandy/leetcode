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
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = sum([sum([elem !=0 for elem in row]) for row in grid])
        y_graph = [0]*n
        z_graph = [0]*n
        
        for i in range(n):
            for j in range(n):
                y_graph[i] = max(y_graph[i],grid[i][j])
                z_graph[j] = max(z_graph[j],grid[i][j])
        area +=sum(y_graph)+sum(z_graph)
        return area

sol = Solution()

# input
grid = [[1,2],[3,4]]

# output
output = sol.projectionArea(grid)
# answer
answer = 17
print(output, answer, answer == output)

# input
grid = [[2]]

# output
output = sol.projectionArea(grid)
# answer
answer = 5
print(output, answer, answer == output)

# input
grid = [[1,0],[0,2]]

# output
output = sol.projectionArea(grid)
# answer
answer = 8
print(output, answer, answer == output)

# input
grid = [[1,1,1],[1,0,1],[1,1,1]]

# output
output = sol.projectionArea(grid)
# answer
answer = 14
print(output, answer, answer == output)

# input
grid = [[2,2,2],[2,1,2],[2,2,2]]

# output
output = sol.projectionArea(grid)
# answer
answer = 21
print(output, answer, answer == output)

# input
grid = [[0]]

# output
output = sol.projectionArea(grid)
# answer
answer = 0
print(output, answer, answer == output)
