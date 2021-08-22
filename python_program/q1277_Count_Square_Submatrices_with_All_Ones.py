from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        square_set = set()
        m,n = len(matrix),len(matrix[0])
        count = 0 
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==1:
                    square_set.add((i,j))
                    count+=1

        while square_set:
            next_set = set()
            for (i,j) in square_set:
                if (i,j+1) in square_set and (i+1,j) in square_set and (i+1,j+1) in square_set:
                    next_set.add((i,j))
                    count+=1
            square_set = next_set                        
        
        return count

sol = Solution()


# input
matrix = [[0]]

# output
output = sol.countSquares(matrix)
# answer
answer = 0
print(output, answer, answer == output)

# input
matrix = [[1]]

# output
output = sol.countSquares(matrix)
# answer
answer = 1
print(output, answer, answer == output)

# input
matrix = [[1,1,1]]

# output
output = sol.countSquares(matrix)
# answer
answer = 3
print(output, answer, answer == output)

# input
matrix = [[1,1,1],[0,1,1]]

# output
output = sol.countSquares(matrix)
# answer
answer = 6
print(output, answer, answer == output)

# input
matrix = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]

# output
output = sol.countSquares(matrix)
# answer
answer = 7
print(output, answer, answer == output)

# input
matrix =[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

# output
output = sol.countSquares(matrix)
# answer
answer = 15
print(output, answer, answer == output)
