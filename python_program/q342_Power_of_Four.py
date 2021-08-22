from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n %4 ==0:
            return self.isPowerOfFour(n//4)
        else:
            return False

sol = Solution()


# input
n = 16

# output
output = sol.isPowerOfFour(n)
# answer
answer = True
print(output, answer, answer == output)

# input
n = 5

# output
output = sol.isPowerOfFour(n)
# answer
answer = False
print(output, answer, answer == output)

# input
n = 1

# output
output = sol.isPowerOfFour(n)
# answer
answer = True
print(output, answer, answer == output)

# input
n = -4

# output
output = sol.isPowerOfFour(n)
# answer
answer = False
print(output, answer, answer == output)
