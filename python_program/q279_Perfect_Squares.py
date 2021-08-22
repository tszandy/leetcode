from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def numSquares(self, n: int) -> int:
        num_square = {}
        square = []
        for i in range(1,n+1):
            if int(sqrt(i))**2 ==i:
                square.append(i)
                num_square[i]=1
                continue
            count_square = float("inf")
            
            for sq in square:
                count_square = min(count_square,num_square[i-sq]+1)
            num_square[i] = count_square
        return num_square[n]
    

sol = Solution()


# input
n = 12
# output
output = sol.numSquares(n)
# answer
answer = 3
print(output, answer, answer == output)

# input
n = 13
# output
output = sol.numSquares(n)
# answer
answer = 2
print(output, answer, answer == output)

# input
n = 8954
# output
output = sol.numSquares(n)
# answer
answer = 2
print(output, answer, answer == output)

# input
n = 2534
# output
output = sol.numSquares(n)
# answer
answer = 3
print(output, answer, answer == output)

# input
n = 1254
# output
output = sol.numSquares(n)
# answer
answer = 3
print(output, answer, answer == output)

# input
n = 983
# output
output = sol.numSquares(n)
# answer
answer = 4
print(output, answer, answer == output)
