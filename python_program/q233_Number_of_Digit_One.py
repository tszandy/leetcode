from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def countDigitOne(self, n: int) -> int:
        length = len(str(n))
        count_1 = 0
        for i in range(1,length+1):
            count_1 += (n//10**i)*(10**(i-1))+min(max(n%(10**i)-10**(i-1)+1,0),10**(i-1))
        return count_1

sol = Solution()


# input
n = 13

# output
output = sol.countDigitOne(n)
# answer
answer = 6
print(output, answer, answer == output)

# input
n = 0

# output
output = sol.countDigitOne(n)
# answer
answer = 0
print(output, answer, answer == output)

# input
n = 1

# output
output = sol.countDigitOne(n)
# answer
answer = 1
print(output, answer, answer == output)

# input
n = 3789217

# output
output = sol.countDigitOne(n)
# answer
answer = 3295850
print(output, answer, answer == output)
