from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.matrix = matrix
        m = len(matrix)
        n = len(matrix[0])
        self.return_list = []
        self.spiral_order_leftupper_to_rightdown((0,0),(m-1,n-1))
        return self.return_list
        
    def spiral_order_leftupper_to_rightdown(self,x,y):
        if x[0]==y[0]:
            for i in range(x[1],y[1]+1):
                self.return_list.append(self.matrix[x[0]][i])
            return        
        if x[1]==y[1]:
            for i in range(x[0],y[0]+1):
                self.return_list.append(self.matrix[i][x[1]])
            return
        for i in range(x[1],y[1]+1):
            self.return_list.append(self.matrix[x[0]][i])
        for i in range(x[0]+1,y[0]+1):
            self.return_list.append(self.matrix[i][y[1]])
        
        self.spiral_order_rightdown_to_leftupper((y[0],y[1]-1),(x[0]+1,x[1]))
    
    def spiral_order_rightdown_to_leftupper(self,x,y):
        if x[0]==y[0]:
            for i in range(y[1],x[1]+1)[::-1]:
                self.return_list.append(self.matrix[x[0]][i])
            return        
        if x[1]==y[1]:
            for i in range(y[0],x[0]+1)[::-1]:
                self.return_list.append(self.matrix[i][x[1]])
            return
        for i in range(y[1],x[1]+1)[::-1]:
            self.return_list.append(self.matrix[x[0]][i])
        for i in range(y[0],x[0])[::-1]:
            self.return_list.append(self.matrix[i][y[1]])
        
        self.spiral_order_leftupper_to_rightdown((y[0],y[1]+1),(x[0]-1,x[1]))
  

sol = Solution()

#2x2
# input
matrix = [[1,2],[3,4]]

# output
output = sol.spiralOrder(matrix)
# answer
answer = [1,2,4,3]
print(output, answer, answer == output)

#2x3
# input
matrix = [[1,2,3],[4,5,6]]

# output
output = sol.spiralOrder(matrix)
# answer
answer = [1,2,3,6,5,4]
print(output, answer, answer == output)

#2x4
# input
matrix = [[1,2,3,4],[5,6,7,8]]

# output
output = sol.spiralOrder(matrix)
# answer
answer = [1,2,3,4,8,7,6,5]
print(output, answer, answer == output)

#3x2
# input
matrix = [[1,2],[3,4],[5,6]]

# output
output = sol.spiralOrder(matrix)
# answer
answer = [1,2,4,6,5,3]
print(output, answer, answer == output)

#3x3
# input
matrix = [[1,2,3],[4,5,6],[7,8,9]]

# output
output = sol.spiralOrder(matrix)
# answer
answer = [1,2,3,6,9,8,7,4,5]
print(output, answer, answer == output)

#3x4
# input
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# output
output = sol.spiralOrder(matrix)
# answer
answer = [1,2,3,4,8,12,11,10,9,5,6,7]
print(output, answer, answer == output)

#4x2
# input
matrix = [[1,2],[3,4],[5,6],[7,8]]

# output
output = sol.spiralOrder(matrix)
# answer
answer = [1,2,4,6,8,7,5,3]
print(output, answer, answer == output)

#4x3
# input
matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

# output
output = sol.spiralOrder(matrix)
# answer
answer = [1,2,3,6,9,12,11,10,7,4,5,8]
print(output, answer, answer == output)

#4x4
# input
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# output
output = sol.spiralOrder(matrix)
# answer
answer = [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
print(output, answer, answer == output)
