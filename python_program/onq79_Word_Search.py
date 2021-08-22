from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        char_to_index = defaultdict(list)
        for i in range(m):
            for j in range(n):
                char_to_index[board[i][j]].append((i,j))
        wl = len(word)
        string_of_length_index_add_1 = defaultdict(set)
        for x,y in char_to_index[word[0]]:
            string_of_length_index_add_1[0].add((x,y))

        for i in range(1,wl):
            for x,y in char_to_index[word[i]]:
                for d_x,d_y in [(0,1),(0,-1),(1,0),(-1,0)]:
                    if (x+d_x,y+d_y) in string_of_length_index_add_1[i-1]:
                        string_of_length_index_add_1[i].add((x,y))
                        break
        return len(string_of_length_index_add_1[wl-1])!=0
            

sol = Solution()

# input
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

word = "ABCCED"

# output
output = sol.exist(board,word)
# answer
answer = True
print(output, answer, answer == output)

# input
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

word = "SEE"

# output
output = sol.exist(board,word)
# answer
answer = True
print(output, answer, answer == output)

# input
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

word = "ABCB"

# output
output = sol.exist(board,word)
# answer
answer = False
print(output, answer, answer == output)
