from typing import List
from collections import Counter,defaultdict,deque
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count,zip_longest
import queue

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        mat = np.array(mat)
        target = np.array(target)
        sum_mat = mat.sum()
        sum_target = target.sum()
        if sum_mat!=sum_target:
            return False
        if (1-(mat==target)).sum()==0:
            return True
        rotate_90_mat = self.rotate_90(mat)
        if (1-(rotate_90_mat==target)).sum()==0:
            return True
        rotate_180_mat = self.rotate_90(rotate_90_mat)
        if (1-(rotate_180_mat==target)).sum()==0:
            return True
        rotate_270_mat = self.rotate_90(rotate_180_mat)
        if (1-(rotate_270_mat==target)).sum()==0:
            return True
        return False

    def rotate_90(self,mat:np.ndarray)-> np.ndarray:
        n = len(mat)
        return_mat = np.zeros(mat.shape)
        for i in range(n):
            for j in range(n):
                return_mat[n-1-j][i] = mat[i][j]
        return return_mat

sol = Solution()

# input
mat = [[0,1],[1,0]]
target = [[1,0],[0,1]]
# output
output = sol.findRotation(mat,target)
# answer
answer = True
print(output, answer, answer == output)

# input
mat = [[0,1],[1,1]]
target = [[1,0],[0,1]]
# output
output = sol.findRotation(mat,target)
# answer
answer = False
print(output, answer, answer == output)

# input
mat = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]
# output
output = sol.findRotation(mat,target)
# answer
answer = True
print(output, answer, answer == output)

# input
mat = [[0]]
target = [[1]]
# output
output = sol.findRotation(mat,target)
# answer
answer = False
print(output, answer, answer == output)
