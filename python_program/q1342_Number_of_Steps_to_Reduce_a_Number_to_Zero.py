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
    def numberOfSteps(self, num: int) -> int:
        binary_string = bin(num)[2:]
        return len(binary_string)+reduce(lambda x,y:x+y,map(lambda x:int(x),binary_string))-1

sol = Solution()

# input

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
