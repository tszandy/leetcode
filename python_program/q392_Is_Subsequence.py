from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        m = len(s)
        n = len(t)
        for i in range(n):
            if s_index>=m:
                return True
            if t[i]==s[s_index]:
                s_index+=1
        if s_index>=m:
            return True
        return False

sol = Solution()


# input
s = "abc"

t = "ahbgdc"

# output
output = sol.isSubsequence(s,t)
# answer
answer = True
print(output, answer, answer == output)

# input
s = "axc"

t = "ahbgdc"

# output
output = sol.isSubsequence(s,t)
# answer
answer = False
print(output, answer, answer == output)

# input
s = ""

t = "ahbgdc"

# output
output = sol.isSubsequence(s,t)
# answer
answer = True
print(output, answer, answer == output)

# input
s = "abc"

t = "abc"

# output
output = sol.isSubsequence(s,t)
# answer
answer = True
print(output, answer, answer == output)
