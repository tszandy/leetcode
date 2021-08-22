from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def fib(self, n: int) -> int:
        store = {}
        store[0] = 0
        store[1] = 1
        for i in range(2,n+1):
            store[i]=store[i-1]+ store[i-2]
        return store[n]

sol = Solution()


# input
n = 0
# output
output = sol.fib(n)
# answer
answer = 0
print(output, answer, answer == output)

# input
n = 1
# output
output = sol.fib(n)
# answer
answer = 1
print(output, answer, answer == output)

# input
n = 2
# output
output = sol.fib(n)
# answer
answer = 1
print(output, answer, answer == output)

# input
n = 3
# output
output = sol.fib(n)
# answer
answer = 2
print(output, answer, answer == output)

# input
n = 4
# output
output = sol.fib(n)
# answer
answer = 3
print(output, answer, answer == output)

# input
n = 30
# output
output = sol.fib(n)
# answer
answer = 832040
print(output, answer, answer == output)
