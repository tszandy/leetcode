from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m*n
        axis_x,axis_y = zip(*ops)
        return min(axis_x)*min(axis_y)

sol = Solution()


# input
m = 3
n = 3
ops = [[2,2],[3,3]]
# output
output = sol.maxCount(m,n,ops)
# answer
answer = 4
print(output, answer, answer == output)

# input
m = 3
n = 3
ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
# output
output = sol.maxCount(m,n,ops)
# answer
answer = 4
print(output, answer, answer == output)

# input
m = 4
n = 4
ops = [[1,2],[3,4]]
# output
output = sol.maxCount(m,n,ops)
# answer
answer = 2
print(output, answer, answer == output)

# input
m = 3
n = 4
ops = []
# output
output = sol.maxCount(m,n,ops)
# answer
answer = 12
print(output, answer, answer == output)
