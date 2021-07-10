from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        count_unique = [
            1,
            9,
            9*9,
            9*9*8,
            9*9*8*7,
            9*9*8*7*6,
            9*9*8*7*6*5,
            9*9*8*7*6*5*4,
            9*9*8*7*6*5*4*3            
        ]
        
        count = 0
        for i in range(n+1):
            count+=count_unique[i]
        return count

sol = Solution()


# input
n = 0

# output
output = sol.countNumbersWithUniqueDigits(n)
# answer
answer = 1
print(output, answer, answer == output)

# input
n = 1

# output
output = sol.countNumbersWithUniqueDigits(n)
# answer
answer = 10
print(output, answer, answer == output)

# input
n = 2

# output
output = sol.countNumbersWithUniqueDigits(n)
# answer
answer = 91
print(output, answer, answer == output)

# input
n = 8

# output
output = sol.countNumbersWithUniqueDigits(n)
# answer
answer = 2345851
print(output, answer, answer == output)
