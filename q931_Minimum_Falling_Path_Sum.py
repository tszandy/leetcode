from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        pre_row = matrix[0]
        next_row = None
        for i in range(1,n):
            next_row = matrix[i]
            for j in range(n):
                min_list = []
                if 0<j:
                    min_list.append(pre_row[j-1])
                if j<n-1:
                    min_list.append(pre_row[j+1])
                min_list.append(pre_row[j])
                next_row[j] += min(min_list)
            pre_row = next_row
        return min(pre_row)

sol = Solution()

# input
matrix = [[2,1,3],[6,5,4],[7,8,9]]

# output
output = sol.minFallingPathSum(matrix)
# answer
answer = 13
print(output, answer, answer == output)

# input
matrix = [[-19,57],[-40,-5]]

# output
output = sol.minFallingPathSum(matrix)
# answer
answer = -59
print(output, answer, answer == output)

# input
matrix = [[-48]]

# output
output = sol.minFallingPathSum(matrix)
# answer
answer = -48
print(output, answer, answer == output)
