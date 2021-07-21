from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        self.iterator = count()
        next(self.iterator)        
        self.matrix = [[0]*n for _ in range(n)]
        self.spiral_order_leftupper_to_rightdown([0,0],[n-1,n-1])
        return self.matrix

    def spiral_order_leftupper_to_rightdown(self,x,y):
        if x[0]==y[0]:
            for i in range(x[1],y[1]+1):
                self.matrix[x[0]][i] = next(self.iterator)
            return        
        if x[1]==y[1]:
            for i in range(x[0],y[0]+1):
                self.matrix[i][x[1]] = next(self.iterator)
            return
        for i in range(x[1],y[1]+1):
            self.matrix[x[0]][i] = next(self.iterator)
        for i in range(x[0]+1,y[0]+1):
            self.matrix[i][y[1]] = next(self.iterator)
        
        self.spiral_order_rightdown_to_leftupper((y[0],y[1]-1),(x[0]+1,x[1]))
    
    def spiral_order_rightdown_to_leftupper(self,x,y):
        if x[0]==y[0]:
            for i in range(y[1],x[1]+1)[::-1]:
                self.matrix[x[0]][i] = next(self.iterator)
            return        
        if x[1]==y[1]:
            for i in range(y[0],x[0]+1)[::-1]:
                self.matrix[i][x[1]] = next(self.iterator)
            return
        for i in range(y[1],x[1]+1)[::-1]:
            self.matrix[x[0]][i] = next(self.iterator)
        for i in range(y[0],x[0])[::-1]:
            self.matrix[i][y[1]] = next(self.iterator)
        
        self.spiral_order_leftupper_to_rightdown((y[0],y[1]+1),(x[0]-1,x[1]))

sol = Solution()


# input
n = 1
# output
output = sol.generateMatrix(n)
# answer
answer = [[1]]
print(output, answer, answer == output)

# input
n = 5
# output
output = sol.generateMatrix(n)
# answer
answer = [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]
print(output, answer, answer == output)

# input
n = 10
# output
output = sol.generateMatrix(n)
# answer
answer = [[1,2,3,4,5,6,7,8,9,10],[36,37,38,39,40,41,42,43,44,11],[35,64,65,66,67,68,69,70,45,12],[34,63,84,85,86,87,88,71,46,13],[33,62,83,96,97,98,89,72,47,14],[32,61,82,95,100,99,90,73,48,15],[31,60,81,94,93,92,91,74,49,16],[30,59,80,79,78,77,76,75,50,17],[29,58,57,56,55,54,53,52,51,18],[28,27,26,25,24,23,22,21,20,19]]
print(output, answer, answer == output)
