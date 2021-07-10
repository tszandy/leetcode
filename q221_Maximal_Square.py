from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        square_set = set()
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="1":
                    square_set.add((i,j))
        
        square_size = 0
        while square_set:
            next_set = set()
            for (i,j) in square_set:
                if (i,j+1) in square_set and (i+1,j) in square_set and (i+1,j+1) in square_set:
                    next_set.add((i,j))
            square_set = next_set                        
            square_size+=1
        return square_size**2

sol = Solution()


# input
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

# output
output = sol.maximalSquare(matrix)
# answer
answer = 4
print(output, answer, answer == output)

# input
matrix = [["0","1"],["1","0"]]

# output
output = sol.maximalSquare(matrix)
# answer
answer = 1
print(output, answer, answer == output)

# input
matrix = [["0"]]

# output
output = sol.maximalSquare(matrix)
# answer
answer = 0
print(output, answer, answer == output)
