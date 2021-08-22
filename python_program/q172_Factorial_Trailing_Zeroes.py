from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count
import queue

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n<5:
            return 0 
        return n//5+self.trailingZeroes(n//5)

sol = Solution()

# input
n = 9735

# output
output = sol.trailingZeroes(n)
# answer
answer = 2431
print(output, answer, answer == output)

# input
n = 7314

# output
output = sol.trailingZeroes(n)
# answer
answer = 1825
print(output, answer, answer == output)

# input
n = 5362

# output
output = sol.trailingZeroes(n)
# answer
answer = 1337
print(output, answer, answer == output)

# input
n = 2753

# output
output = sol.trailingZeroes(n)
# answer
answer = 686
print(output, answer, answer == output)

# input
n = 3

# output
output = sol.trailingZeroes(n)
# answer
answer = 0
print(output, answer, answer == output)

# input
n = 5

# output
output = sol.trailingZeroes(n)
# answer
answer = 1
print(output, answer, answer == output)

# input
n = 0

# output
output = sol.trailingZeroes(n)
# answer
answer = 0
print(output, answer, answer == output)
