from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbor_dict = defaultdict(int)
        m,n = len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]==1:
                    cond_1 = 0<i
                    cond_2 = 0<j
                    cond_3 = i<m
                    cond_4 = j<n
                    if cond_1:
                        neighbor_dict[(i-1,j)]+=1
                    if cond_2:
                        neighbor_dict[(i,j-1)]+=1
                    if cond_3:
                        neighbor_dict[(i+1,j)]+=1
                    if cond_4:
                        neighbor_dict[(i,j+1)]+=1
                    if cond_1 and cond_2:
                        neighbor_dict[(i-1,j-1)]+=1
                    if cond_1 and cond_4:
                        neighbor_dict[(i-1,j+1)]+=1
                    if cond_3 and cond_2:
                        neighbor_dict[(i+1,j-1)]+=1
                    if cond_3 and cond_4:
                        neighbor_dict[(i+1,j+1)]+=1
        for i in range(m):
            for j in range(n):
                if board[i][j]==1:
                    if not (neighbor_dict[(i,j)]==2 or neighbor_dict[(i,j)]==3):
                        board[i][j]=0
                else:
                    if neighbor_dict[(i,j)]==3:
                        board[i][j]=1
        return board

sol = Solution()


# input
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# output
output = sol.gameOfLife(board)
# answer
answer = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
print(output, answer, answer == output)

# input
board = [[1,1],[1,0]]
# output
output = sol.gameOfLife(board)
# answer
answer = [[1,1],[1,1]]
print(output, answer, answer == output)
