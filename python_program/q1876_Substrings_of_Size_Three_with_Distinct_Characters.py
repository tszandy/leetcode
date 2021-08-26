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
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        count_good = 0
        for i in range(n-2):
            if s[i]!=s[i+1] and s[i]!=s[i+2] and s[i+1]!=s[i+2]:
                count_good +=1
        return count_good

sol = Solution()

# input
"xyzzaz"
"aababcabc"

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
