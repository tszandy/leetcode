from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def integerBreak(self, n: int) -> int:
        product = {}
        product[2]=1
        product[3]=2
        product[4]=4
        product[5]=6
        product[6]=9
        for i in range(7,n+1):
            product[i]=max(product[i-2]*2,product[i-3]*3,product[i-4]*4)
        return product[n]

sol = Solution()


# input
n = 2
# output
output = sol.integerBreak(n)
# answer
answer = 1
print(output, answer, answer == output)

# input
n = 10
# output
output = sol.integerBreak(n)
# answer
answer = 36
print(output, answer, answer == output)

# input
n = 15
# output
output = sol.integerBreak(n)
# answer
answer = 243
print(output, answer, answer == output)

# input
n = 30
# output
output = sol.integerBreak(n)
# answer
answer = 59049
print(output, answer, answer == output)

# input
n = 58
# output
output = sol.integerBreak(n)
# answer
answer = 1549681956
print(output, answer, answer == output)
