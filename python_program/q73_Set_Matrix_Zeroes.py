from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix),len(matrix[0])
        row_set = set(range(n))
        col_set = set(range(m))
        
        row_zero_set = set()
        col_zero_set = set()
        
        for i in range(n):
            for j in list(col_set):
                if matrix[i][j]==0:
                    row_zero_set.add(i)
                    col_zero_set.add(j)
        
        for i in row_zero_set:
            for j in range(m):
                matrix[i][j] = 0

        for j in col_zero_set:
            for i in range(n):
                matrix[i][j] = 0
        return matrix


sol = Solution()


# input
matrix = [[1,1,1],[1,0,1],[1,1,1]]
# output
output = sol.setZeroes(matrix)
# answer
answer = [[1,0,1],[0,0,0],[1,0,1]]
print(output, answer, answer == output)

# input
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# output
output = sol.setZeroes(matrix)
# answer
answer = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
print(output, answer, answer == output)

# input
matrix = [[0,1,2,0],[3,0,5,2],[1,3,1,5]]
# output
output = sol.setZeroes(matrix)
# answer
answer = [[0,0,0,0],[0,0,0,0],[0,0,1,0]]
print(output, answer, answer == output)

# input
matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
# output
output = sol.setZeroes(matrix)
# answer
answer = [[0,0,0,0],[0,0,0,4],[0,0,0,0],[0,0,0,3],[0,0,0,0]]
print(output, answer, answer == output)
