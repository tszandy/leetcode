from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def climbStairs(self, n: int) -> int:
        answer = [0]*n
        if n <=2:
            return n           
        answer[0]=1
        answer[1]=2
        if n >2:
            for i in range(2,n):
                answer[i] = answer[i-1] + answer[i-2]
        return answer[n-1]

sol = Solution()


# input
n = 1
# output
output = sol.climbStairs(n)
# answer
answer = 1
print(output, answer, answer == output)

# input
n = 2
# output
output = sol.climbStairs(n)
# answer
answer = 2
print(output, answer, answer == output)

# input
n = 3
# output
output = sol.climbStairs(n)
# answer
answer = 3
print(output, answer, answer == output)

# input
n = 45
# output
output = sol.climbStairs(n)
# answer
answer = 1836311903
print(output, answer, answer == output)
