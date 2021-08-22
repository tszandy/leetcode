from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                square_sum = i**2+j**2
                if int(sqrt(square_sum)) == sqrt(square_sum) and sqrt(square_sum)<=n:
                    count+=2
        return count

sol = Solution()


# input
n = 5

# output
output = sol.countTriples(n)
# answer
answer = 2
print(output, answer, answer == output)

# input
n = 10

# output
output = sol.countTriples(n)
# answer
answer = 4
print(output, answer, answer == output)

# input
n = 12

# output
output = sol.countTriples(n)
# answer
answer = 4
print(output, answer, answer == output)

# input
n = 19

# output
output = sol.countTriples(n)
# answer
answer = 10
print(output, answer, answer == output)

# input
n = 20

# output
output = sol.countTriples(n)
# answer
answer = 12
print(output, answer, answer == output)

# input
n = 250

# output
output = sol.countTriples(n)
# answer
answer = 330
print(output, answer, answer == output)
