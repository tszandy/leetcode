from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_counter = defaultdict(list)
        col_counter = defaultdict(list)
        sqr_counter = defaultdict(list)
        for i in range(9):
            for j in range(9):
                e = board[i][j]
                if e != ".":
                    if int(e) <=9 and int(e) >=1 and e not in row_counter[i]and e not in col_counter[j] and e not in sqr_counter[i//3+j//3*3]:
                        row_counter[i].append(e)
                        col_counter[j].append(e)
                        sqr_counter[i//3+j//3*3].append(e)
                    else:return False
        return True

sol = Solution()


# input
board = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
# output
output = sol.isValidSudoku(board)
# answer
answer = True
print(output, answer, answer == output)

# input
board = \
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
# output
output = sol.isValidSudoku(board)
# answer
answer = False
print(output, answer, answer == output)
