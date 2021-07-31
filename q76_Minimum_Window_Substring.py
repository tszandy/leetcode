from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count

class Counter(Counter):
    def __ge__(self,other):
        return all(self[key]>=other[key] for key in other)
    def __lt__(self,other):
        return all(self[key]<other[key] for key in other)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n_s = len(s)
        n_t = len(t)
        if n_s<n_t:
            return ""
        t_counter = Counter(t)

        l = 0
        r = 0
        s_counter = Counter()
        minimum_count = float("inf")
        substring = ""
        cond = s_counter>=t_counter
        while r < n_s or cond:
            if not cond:
                s_counter[s[r]]+=1
                r+=1
            else:
                if r-l<minimum_count:
                    minimum_count = r-l
                    substring = s[l:r]
                s_counter[s[l]]-=1
                l+=1
            cond = s_counter>=t_counter
            
        return substring

sol = Solution()

# input
s = "ADOBECODEBANC"

t = "ABC"

# output
output = sol.minWindow(s,t)
# answer
answer = ""
print(output, answer, answer == output)

# input
s = "a"

t = "a"

# output
output = sol.minWindow(s,t)
# answer
answer = ""
print(output, answer, answer == output)

# input
s = "a"

t = "aa"

# output
output = sol.minWindow(s,t)
# answer
answer = ""
print(output, answer, answer == output)
