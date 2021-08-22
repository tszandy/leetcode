from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_counter = defaultdict(set)
        col_counter = defaultdict(set)
        sqr_counter = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                e = board[i][j]
                if e != ".":
                    if int(e) <=9 and int(e) >=1 and e not in row_counter[i]and e not in col_counter[j] and e not in sqr_counter[i//3+j//3*3]:
                        row_counter[i].add(e)
                        col_counter[j].add(e)
                        sqr_counter[i//3+j//3*3].add(e)
                
        def backtracking(i,j,board,get_solution):
            if i==0 and j==9:
                get_solution[0][0] = True
                return board
            if board[i][j]==".":
                for k in range(1,10):
                    e = str(k)
                    if e not in row_counter[i] and e not in col_counter[j] and e not in sqr_counter[i//3+j//3*3]:
                        board[i][j] = e
                        row_counter[i].add(e)
                        col_counter[j].add(e)
                        sqr_counter[i//3+j//3*3].add(e)
                        backtracking((i+1)%9, j+(i+1)//9,board,get_solution)
                        if get_solution[0][0]:
                            return board
                        board[i][j] = "."
                        row_counter[i].remove(e)
                        col_counter[j].remove(e)
                        sqr_counter[i//3+j//3*3].remove(e)
            else:
                backtracking((i+1)%9, j+(i+1)//9,board,get_solution)
        backtracking(0,0,board,[[False]]) 
        return board

sol = Solution()


# input
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# output
output = sol.solveSudoku(board)
# answer
answer = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
print(output, answer, answer == output)

# input
board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
# output
output = sol.solveSudoku(board)
# answer
answer = [["5","1","9","7","4","8","6","3","2"],["7","8","3","6","5","2","4","1","9"],["4","2","6","1","3","9","8","7","5"],["3","5","7","9","8","6","2","4","1"],["2","6","4","3","1","7","5","9","8"],["1","9","8","5","2","4","3","6","7"],["9","7","5","8","6","3","1","2","4"],["8","3","2","4","9","1","7","5","6"],["6","4","1","2","7","5","9","8","3"]]
print(output, answer, answer == output)
