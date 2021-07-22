from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        gcd_n1_n2 = gcd(n1,n2)
        n1 //= gcd_n1_n2
        n2 //= gcd_n1_n2
        s1 *= n1
        s2 *= n2
        return self.count_sub_string(s1,s2)
    def count_sub_string(self,s1,s2):
        n_s1 = len(s1)
        n_s2 = len(s2)
        if n_s2>n_s1:
            return 0
        l_s1 = 0
        l_s2 = 0
        count = 0
        while l_s1<n_s1:
            if s1[l_s1] == s2[l_s2]:
                l_s1+=1
                l_s2+=1
                if l_s2 == n_s2:
                    count+=1
                    l_s2 = 0
            else:
                l_s1+=1
        return count


sol = Solution()

# input
s1 = "acb"

n1 = 4

s2 = "ab"

n2 = 2

# output
output = sol.getMaxRepetitions(s1,n1,s2,n2)
# answer
answer = 2
print(output, answer, answer == output)

# input
s1 = "acb"

n1 = 1

s2 = "acb"

n2 = 1

# output
output = sol.getMaxRepetitions(s1,n1,s2,n2)
# answer
answer = 1
print(output, answer, answer == output)

# input
s1 = "aaaaa"

n1 = 4

s2 = "aa"

n2 = 2

# output
output = sol.getMaxRepetitions(s1,n1,s2,n2)
# answer
answer = 5
print(output, answer, answer == output)

# input
s1 = "phqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikef"

n1 = 1000000

s2 = "fmznimkkasvwsrenzkycxfxtlsgypsfad"

n2 = 333

# output
output = sol.getMaxRepetitions(s1,n1,s2,n2)
# answer
answer = 5
print(output, answer, answer == output)
