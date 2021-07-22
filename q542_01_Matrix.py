from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        track_one = []
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    track_one.append((i,j))
                    mat[i][j] = float("inf")
        while track_one:
            store_change = {}
            for x,y in list(track_one):
                right_elem = float("inf")
                if y+1<n:
                    right_elem = mat[x][y+1]
                left_elem = float("inf")
                if 0<=y-1:
                    left_elem = mat[x][y-1]
                down_elem = float("inf")
                if x+1<m:
                    down_elem = mat[x+1][y]
                up_elem = float("inf")
                if 0<=x-1:
                    up_elem = mat[x-1][y]
                min_elem = min(right_elem,left_elem,down_elem,up_elem)
                if min_elem != float("inf"):
                    store_change[(x,y)] = min_elem+1
                    track_one.remove((x,y))
            for key,val in store_change.items():
                mat[key[0]][key[1]]=val
        return mat

sol = Solution()

# input
mat = [[0,0,0],[0,1,0],[0,0,0]]

# output
output = sol.updateMatrix(mat)
# answer
answer = [[0,0,0],[0,1,0],[0,0,0]]
print(output, answer, answer == output)

# input
mat = [[0,0,0],[0,1,0],[1,1,1]]

# output
output = sol.updateMatrix(mat)
# answer
answer = [[0,0,0],[0,1,0],[1,2,1]]
print(output, answer, answer == output)
