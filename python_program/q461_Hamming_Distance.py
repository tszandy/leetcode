from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(map(lambda x:int(x),bin(x^y)[2:]))


sol = Solution()


# input
x = 1
y = 4
# output
output = sol.hammingDistance(x,y)
# answer
answer = 2
print(output, answer, answer == output)

# input
x = 3
y = 1
# output
output = sol.hammingDistance(x,y)
# answer
answer = 1
print(output, answer, answer == output)
