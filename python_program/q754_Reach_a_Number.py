from typing import List
from collections import Counter,defaultdict,deque
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count,zip_longest
import queue

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        s = 0
        i = 1
        while s<target:
            s+=i
            i+=1
        if (s-target)%2==0:
            return i-1
        elif i%2==1:
            return i
        else:
            return i+1

sol = Solution()

# input
target = 5

# output
output = sol.reachNumber(target)
# answer
answer = 5
print(output, answer, answer == output)

# input
target = 10

# output
output = sol.reachNumber(target)
# answer
answer = 4
print(output, answer, answer == output)

# input
target = -3

# output
output = sol.reachNumber(target)
# answer
answer = 2
print(output, answer, answer == output)

# input
target = 1532

# output
output = sol.reachNumber(target)
# answer
answer = 55
print(output, answer, answer == output)

# input
target = -1532

# output
output = sol.reachNumber(target)
# answer
answer = 55
print(output, answer, answer == output)
