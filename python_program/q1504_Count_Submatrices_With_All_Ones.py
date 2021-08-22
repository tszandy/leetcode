from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m,n = len(mat),len(mat[0])
        store_rectangles = defaultdict(set)
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    store_rectangles[(i,j)].add("1x1")
                    if 0<i and 0<j:
                        for string in store_rectangles[(i-1,j)]:
                            a,b = string.split("x")
                            if "x".join([str(int(a)+1),str(int(b)-1)]) in store_rectangles[(i,j-1)]:
                                store_rectangles[(i,j)].add("x".join([str(int(a)+1),b]))
                    if 0<j:
                        for string in store_rectangles[(i,j-1)]:
                            a,b = string.split("x")
                            if a == "1":
                                store_rectangles[(i,j)].add("x".join([a,str(int(b)+1)]))
                    if 0<i:
                        for string in store_rectangles[(i-1,j)]:
                            a,b = string.split("x")
                            if b == "1":
                                store_rectangles[(i,j)].add("x".join([str(int(a)+1),b]))
        return sum(map(lambda x:len(x),store_rectangles.values()))

sol = Solution()

# input
mat = [[1,0,1],[1,1,0],[1,1,0]]

# output
output = sol.numSubmat(mat)
# answer
answer = 13
print(output, answer, answer == output)

# input
mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]

# output
output = sol.numSubmat(mat)
# answer
answer = 24
print(output, answer, answer == output)

# input
mat = [[1,1,1,1,1,1]]

# output
output = sol.numSubmat(mat)
# answer
answer = 21
print(output, answer, answer == output)

# input
mat = [[1,0,1],[0,1,0],[1,0,1]]

# output
output = sol.numSubmat(mat)
# answer
answer = 5
print(output, answer, answer == output)

# input
mat = [[0,0,0],[0,0,0],[0,1,1],[1,1,0],[0,1,1]]

# output
output = sol.numSubmat(mat)
# answer
answer = 12
print(output, answer, answer == output)

# input
mat = [[1,1,1,1,0,1,0],[1,1,1,0,0,0,1],[0,1,1,1,1,0,0],[1,1,0,1,1,0,1],[1,0,0,0,0,0,1],[1,1,0,1,1,1,1],[1,1,0,0,1,1,1]]

# output
output = sol.numSubmat(mat)
# answer
answer = 96
print(output, answer, answer == output)
