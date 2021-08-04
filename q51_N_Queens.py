from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        row_count = defaultdict(int)
        col_count = defaultdict(int)
        cross_count = defaultdict(int)
        rcross_count = defaultdict(int)
        queen_count = [0]
        return_list = []
        board = [['.' for _ in range(n)]for _ in range(n)]        
        
        def backtracking(row):
            if queen_count[0] == n:
                return_list.append(list(map(lambda x:"".join(x),board)))
                return
            if row == n:
                return
            for col in range(self.n):
                if row_count[row] == 0 and col_count[col] == 0 and cross_count[(col-row)] == 0 and rcross_count[(col+row)] == 0:
                    board[row][col] = "Q"
                    row_count[row]+=1
                    col_count[col]+=1
                    cross_count[(col-row)]+=1
                    rcross_count[(col+row)]+=1
                    queen_count[0]+=1
                    backtracking(row+1)
                    board[row][col] = "."
                    row_count[row]-=1
                    col_count[col]-=1
                    cross_count[(col-row)]-=1
                    rcross_count[(col+row)]-=1
                    queen_count[0]-=1
        backtracking(0)
        
        return return_list                
                
sol = Solution()


# input
n = 4
# output
output = sol.solveNQueens(n)
# answer
answer = [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
print(output, answer, answer == output)
