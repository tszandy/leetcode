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
    def minNumberOperations(self, target: List[int]) -> int:
        current = 0
        record = 0 
        for i in target:
            if i > current:
                record += i-current
                current = i
            else:
                current = i
        return record

sol = Solution()

# input
target = [1,2,3,2,1]

# output
output = sol.minNumberOperations(target)
# answer
answer = 3

print(output, answer, answer == output)

# input
target = [3,1,1,2]

# output
output = sol.minNumberOperations(target)
# answer
answer = 4

print(output, answer, answer == output)

# input
target = [3,1,5,4,2]

# output
output = sol.minNumberOperations(target)
# answer
answer = 7

print(output, answer, answer == output)

# input
target = [1,1,1,1]

# output
output = sol.minNumberOperations(target)
# answer
answer = 1

print(output, answer, answer == output)
