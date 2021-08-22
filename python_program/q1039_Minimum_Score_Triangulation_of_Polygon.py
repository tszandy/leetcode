from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        l = 0
        r = n-1
        store_score = {}
        def min_score_triangulation(l,r):
            if (l,r) in store_score:
                return store_score[(l,r)]
            if r-l==2:
                store_score[(l,r)] = values[l]*values[l+1]*values[l+2]
                return store_score[(l,r)]
            if r-l<2:
                return 0
            score_list = []
            for i in range(l+1,r):
                score_list.append(values[l]*values[r]*values[i]+min_score_triangulation(l,i)+min_score_triangulation(i,r))
            store_score[(l,r)] = min(score_list)
            return store_score[(l,r)]
        min_score_triangulation(l,r)
        return store_score[(l,r)]

    def minScoreTriangulation_1(self, values: List[int]) -> int:
        n = len(values)
        l = 0
        r = n-1
        store_score = {}
        def min_score_triangulation(l,r):
            if (l,r) in store_score:
                return store_score[(l,r)]
            if r-l==2:
                store_score[(l,r)] = values[l]*values[l+1]*values[l+2]
                return store_score[(l,r)]
            left  = values[l]*values[l+1]*values[r]+min_score_triangulation(l+1,r)
            right = values[l]*values[r-1]*values[r]+min_score_triangulation(l,r-1)
            store_score[(l,r)] = min(left,right)
            return store_score[(l,r)]
        min_score_triangulation(l,r)
        return store_score[(l,r)]

sol = Solution()


# input
values = [1,2,3]
# output
output = sol.minScoreTriangulation(values)
# answer
answer = 6
print(output, answer, answer == output)

# input
values = [3,7,4,5]
# output
output = sol.minScoreTriangulation(values)
# answer
answer = 144
print(output, answer, answer == output)

# input
values = [1,3,1,4,1,5]
# output
output = sol.minScoreTriangulation(values)
# answer
answer = 13
print(output, answer, answer == output)

# input
values = [3,7,4,5,1,23,12,1,5,5,3,2,1,4]
# output
output = sol.minScoreTriangulation(values)
# answer
answer = 421
print(output, answer, answer == output)
