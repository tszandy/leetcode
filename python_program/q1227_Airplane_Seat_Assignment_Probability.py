from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n ==1:
            return 1
        else:
            return 0.5


sol = Solution()


# input
n = 1
# output
output = sol.nthPersonGetsNthSeat(n)
# answer
answer = 1
print(output, answer, answer == output)

# input
n = 2
# output
output = sol.nthPersonGetsNthSeat(n)
# answer
answer = 0.5
print(output, answer, answer == output)

# input
n = 5000
# output
output = sol.nthPersonGetsNthSeat(n)
# answer
answer = 0.5
print(output, answer, answer == output)
