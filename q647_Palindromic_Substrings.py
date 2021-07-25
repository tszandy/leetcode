from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            cur = [0]*n
            cur[i] = 1
            count+=1
            for j in range(i):
                cur[j] = s[i]==s[j] and (i-j == 1 or prev[j+1])
                count+=cur[j]
            prev = cur
        return count

    def countSubstrings_1(self, s: str) -> int:
        n = count = len(s)
        for i in range(n-1,-1,-1):
            cur = [0]*n
            cur[i] = 1
            for j in range(i+1,n):
                cur[j] = s[i] == s[j] and (j-i == 1 or prev[j-1])
                count += cur[j]
            prev = cur
        return count    

sol = Solution()

# input
s = "s"

# output
output = sol.countSubstrings(s)
# answer
answer = 1
print(output, answer, answer == output)

# input
s = "abc"

# output
output = sol.countSubstrings(s)
# answer
answer = 3
print(output, answer, answer == output)

# input
s = "aaa"

# output
output = sol.countSubstrings(s)
# answer
answer = 6
print(output, answer, answer == output)

# input
s = "jfdkslajfkljktljewalktjaijgkasjgkljsajfjfjjdfs"

# output
output = sol.countSubstrings(s)
# answer
answer = 51
print(output, answer, answer == output)
