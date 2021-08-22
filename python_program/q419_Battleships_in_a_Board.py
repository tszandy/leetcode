from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m,n = len(board),len(board[0])
        visited_battle_ship = set()
        count_ship = 0
        for i in range(m):
            for j in range(n):
                field = board[i][j]
                if field == "X" and (i,j) not in visited_battle_ship:
                    count_ship+=1
                    visited_battle_ship.add((i,j))
                    i_p,j_p = i+1,j
                    while i_p<m and board[i_p][j_p]=="X":
                        visited_battle_ship.add((i_p,j_p))
                        i_p = i_p+1
                    i_p,j_p = i,j+1
                    while j_p<n and board[i_p][j_p]=="X":
                        visited_battle_ship.add((i_p,j_p))
                        j_p = j_p+1
        return count_ship

sol = Solution()


# input
board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
# output
output = sol.countBattleships(board)
# answer
answer = 2
print(output, answer, answer == output)

# input
board = [["."]]
# output
output = sol.countBattleships(board)
# answer
answer = 0
print(output, answer, answer == output)
