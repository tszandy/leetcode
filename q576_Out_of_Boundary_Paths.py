from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        return self.count_path(m,n,maxMove,startRow,startColumn)%(10**9 + 7)
    @lru_cache(None)
    def count_path(self,m,n,max_move,row,col):
        if row<0 or row>=m or col<0 or col>=n:
            return 1
        if max_move == 0:
            return 0 
        path_1 = self.count_path(m,n,max_move-1,row+1,col)
        path_2 = self.count_path(m,n,max_move-1,row-1,col)
        path_3 = self.count_path(m,n,max_move-1,row,col+1)
        path_4 = self.count_path(m,n,max_move-1,row,col-1)
        return (path_1+path_2+path_3+path_4)%(10**9 + 7)

sol = Solution()

# input
m = 2

n = 2

maxMove = 2

startRow = 0

startColumn = 0

# output
output = sol.findPaths(m,n,maxMove,startRow,startColumn)
# answer
answer = 6
print(output, answer, answer == output)

# input
m = 1

n = 3

maxMove = 3

startRow = 0

startColumn = 1

# output
output = sol.findPaths(m,n,maxMove,startRow,startColumn)
# answer
answer = 12
print(output, answer, answer == output)

# input
m = 8

n = 50

maxMove = 23

startRow = 5

startColumn = 26

# output
output = sol.findPaths(m,n,maxMove,startRow,startColumn)
# answer
answer = 914783380
print(output, answer, answer == output)
