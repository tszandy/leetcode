from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_counter = Counter(s)
        for i in list(s_counter.keys()):
            if s_counter[i]!=1:
                del s_counter[i]
        if not s_counter:
            return -1
        for i,e in enumerate(s):
            if e in s_counter:
                return i

sol = Solution()

s = "leetcode"
print(sol.firstUniqChar(s))

s = "loveleetcode"
print(sol.firstUniqChar(s))

s = "aabb"
print(sol.firstUniqChar(s))
