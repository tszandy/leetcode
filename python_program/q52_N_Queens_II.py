from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count
import queue

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.n = n
        row_count = defaultdict(int)
        col_count = defaultdict(int)
        cross_count = defaultdict(int)
        rcross_count = defaultdict(int)
        queen_count = [0]
        return_list_count = [0]
        board = [['.' for _ in range(n)]for _ in range(n)]        
        
        def backtracking(row):
            if queen_count[0] == n:
                return_list_count[0]+=1
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
        
        return return_list_count[0]
                


sol = Solution()

# input
1
2
3
4
5
6
7
8
9

# output
output = sol.totalNQueens(n)
# answer
answer = ""
print(output, answer, answer == output)
