from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def tribonacci(self, n: int) -> int:
        store = {}
        store[0] = 0
        store[1] = 1
        store[2] = 1
        for i in range(3,n+1):
            store[i]=store[i-1]+ store[i-2]+store[i-3]
        return store[n]


sol = Solution()


# input
n = 0
# output
output = sol.tribonacci(n)
# answer
answer = 0
print(output, answer, answer == output)

# input
n = 1
# output
output = sol.tribonacci(n)
# answer
answer = 1
print(output, answer, answer == output)

# input
n = 2
# output
output = sol.tribonacci(n)
# answer
answer = 1
print(output, answer, answer == output)

# input
n = 3
# output
output = sol.tribonacci(n)
# answer
answer = 2
print(output, answer, answer == output)

# input
n = 4
# output
output = sol.tribonacci(n)
# answer
answer = 4
print(output, answer, answer == output)

# input
n = 25
# output
output = sol.tribonacci(n)
# answer
answer = 1389537
print(output, answer, answer == output)
