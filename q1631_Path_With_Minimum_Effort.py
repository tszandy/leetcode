from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        columns = len(heights[0])
        hq = [(0,(0,0))]
        minimum_effort_reach = {}
        while hq:
            effort, cell_index = heappop(hq)
            i,j = cell_index
            if cell_index not in minimum_effort_reach:
                minimum_effort_reach[cell_index] = effort
                if 0<i:
                    if (i-1,j) not in minimum_effort_reach:
                        next_effort = max(abs(heights[i-1][j]-heights[i][j]),effort)
                        heappush(hq,(next_effort,(i-1,j)))
                if i<rows-1:
                    if (i+1,j) not in minimum_effort_reach:
                        next_effort = max(abs(heights[i+1][j]-heights[i][j]),effort)
                        heappush(hq,(next_effort,(i+1,j)))
                if 0<j:
                    if (i,j-1) not in minimum_effort_reach:
                        next_effort = max(abs(heights[i][j-1]-heights[i][j]),effort)
                        heappush(hq,(next_effort,(i,j-1)))
                if j<columns-1:
                    if (i,j+1) not in minimum_effort_reach:
                        next_effort = max(abs(heights[i][j+1]-heights[i][j]),effort)
                        heappush(hq,(next_effort,(i,j+1)))
            if (rows-1,columns-1) in minimum_effort_reach:
                return minimum_effort_reach[(rows-1,columns-1)]
        
        
        

sol = Solution()


# input
heights = [[1,2,2],[3,8,2],[5,3,5]]
# output
output = sol.minimumEffortPath(heights)
# answer
answer = 2
print(output, answer, answer == output)

# input
heights = [[1,2,3],[3,8,4],[5,3,5]]
# output
output = sol.minimumEffortPath(heights)
# answer
answer = 1
print(output, answer, answer == output)

# input
heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# output
output = sol.minimumEffortPath(heights)
# answer
answer = 0
print(output, answer, answer == output)

# input
heights = [[1,2,2,2],[3,8,2,2],[5,3,5,3]]
# output
output = sol.minimumEffortPath(heights)
# answer
answer = 1
print(output, answer, answer == output)

# input
heights = [[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]]
# output
output = sol.minimumEffortPath(heights)
# answer
answer = 5
print(output, answer, answer == output)
