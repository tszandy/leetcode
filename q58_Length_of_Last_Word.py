from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_list = s.split()
        if len(split_list)==0:
            return 0
        else:
            return len(split_list[-1])

sol = Solution()


# input
s = "Hello World"

# output
output = sol.lengthOfLastWord(s)
# answer
answer = 5
print(output, answer, answer == output)

# input
s = " "

# output
output = sol.lengthOfLastWord(s)
# answer
answer = 0
print(output, answer, answer == output)

# input
s = "a"

# output
output = sol.lengthOfLastWord(s)
# answer
answer = 1
print(output, answer, answer == output)

# input
s = "a "

# output
output = sol.lengthOfLastWord(s)
# answer
answer = 1
print(output, answer, answer == output)
