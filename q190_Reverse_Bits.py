from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count
import queue

class Solution:
    def reverseBits(self, n: int) -> int:
        bin_num = bin(n)[2:]
        bin_num = "0"*(32-len(bin_num))+bin_num
        return int(bin_num[::-1],2)


sol = Solution()

# input
n = 0b10100101000001111010011100

# output
output = sol.reverseBits(n)
# answer
answer = 964176192
print(output, answer, answer == output)

# input
n = 0b11111111111111111111111111111101

# output
output = sol.reverseBits(n)
# answer
answer = 3221225471
print(output, answer, answer == output)
