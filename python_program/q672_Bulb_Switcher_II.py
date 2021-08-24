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
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1
        if n ==1:
            return 2
        elif n ==2:
            if presses==1:
                return 3
            else:
                return 4
        else:
            if presses == 1:
                return 4
            elif presses == 2:
                return 7
            else:
                return 8

sol = Solution()

# input
n = 1

presses = 1

# output
output = sol.flipLights(n,presses)
# answer
answer = 2

print(output, answer, answer == output)

# input
n = 2

presses = 1

# output
output = sol.flipLights(n,presses)
# answer
answer = 3

print(output, answer, answer == output)

# input
n = 3

presses = 1

# output
output = sol.flipLights(n,presses)
# answer
answer = 4

print(output, answer, answer == output)

# input
n = 50

presses = 50

# output
output = sol.flipLights(n,presses)
# answer
answer = 8

print(output, answer, answer == output)

# input
n = 4

presses = 1

# output
output = sol.flipLights(n,presses)
# answer
answer = 4

print(output, answer, answer == output)

# input
n = 5

presses = 2

# output
output = sol.flipLights(n,presses)
# answer
answer = 7

print(output, answer, answer == output)

# input
n = 7

presses = 2

# output
output = sol.flipLights(n,presses)
# answer
answer = 7

print(output, answer, answer == output)

# input
n = 9

presses = 2

# output
output = sol.flipLights(n,presses)
# answer
answer = 7

print(output, answer, answer == output)
