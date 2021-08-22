from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        h ,w = len(matrix),len(matrix[0])
        self.dp = {}
        self.dp[(0,0)] = matrix[0][0]
        for i in range(1,h):
            self.dp[(i,0)]=self.dp[(i-1,0)]+matrix[i][0]
        for j in range(1,w):
            self.dp[(0,j)]=self.dp[(0,j-1)]+matrix[0][j]
        for i in range(1,h):
            for j in range(1,w):
                self.dp[(i,j)] = self.dp[(i-1,j)]+self.dp[(i,j-1)]-self.dp[(i-1,j-1)]+matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_region = 0
        sum_region += self.dp[(row2,col2)]
        if row1!=0 and col1!=0:
            sum_region -= self.dp[(row2,col1-1)]
            sum_region -= self.dp[(row1-1,col2)]
            sum_region += self.dp[(row1-1,col1-1)]
        elif row1 != 0:
            sum_region -= self.dp[(row1-1,col2)]
        elif col1 != 0:
            sum_region -= self.dp[(row2,col1-1)]

        return sum_region

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


sol = Solution()


# input

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
