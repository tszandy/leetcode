from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count

class Solution:
#not working
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        lcs = self.get_longestCommonSubsequence(s1,s2)
        n = len(lcs)
        sum_count = 0
        l_lcs = 0
        for c in s1:
            if l_lcs<n and lcs[l_lcs] == c:
                    l_lcs+=1
                    continue
            sum_count += ord(c)
        l_lcs = 0
        for c in s2:
            if l_lcs<n and lcs[l_lcs] == c:
                    l_lcs+=1
                    continue
            sum_count += ord(c)
        return sum_count
        
    def get_longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp =defaultdict(list)
        dp[(-1,-1)].append((0,(-1,-1)))
        for i in range(m):
            dp[(i,-1)].append((0,(-1,-1)))
        for i in range(n):
            dp[(-1,i)].append((0,(-1,-1)))

        for i in range(m):
            c1 = text1[i]
            for j in range(n):
                c2 = text2[j]
                if c1==c2:
                    dp[(i,j)].append((dp[(i-1,j-1)][0][0]+1,(i-1,j-1)))
                else:
                    if dp[(i-1,j)][0][0] > dp[(i,j-1)][0][0]:
                        dp[(i,j)].append((dp[(i-1,j)][0][0],(i-1,j)))
                    else:
                        dp[(i,j)].append((dp[(i,j-1)][0][0],(i,j-1)))

        max_sub_count = 0
        max_sub_index = (None,None)
        for i in range(m):
            for j in range(n):
                if max_sub_count<dp[(i,j)][0][0]:
                    max_sub_count,max_sub_index = dp[(i,j)][0][0],(i,j)
        return_str = ""
        while max_sub_count:
            next_sub_index = dp[max_sub_index][0][1]
            next_sub_count = dp[next_sub_index][0][0]
            if next_sub_count != max_sub_count:
                return_str+=text1[max_sub_index[0]]
            max_sub_count,max_sub_index = next_sub_count,next_sub_index
        return return_str[::-1]


sol = Solution()

# input
s1 = "a"

s2 = "b"

# output
output = sol.minimumDeleteSum(s1,s2)
# answer
answer = 195
print(output, answer, answer == output)

# input
s1 = "sea"

s2 = "eat"

# output
output = sol.minimumDeleteSum(s1,s2)
# answer
answer = 231
print(output, answer, answer == output)

sol = Solution()

# input
s1 = "delete"

s2 = "leet"

# output
output = sol.minimumDeleteSum(s1,s2)
# answer
answer = 403
print(output, answer, answer == output)
# input
s1 = "vwojt"

s2 = "saqhgdrarwntji"

# output
output = sol.minimumDeleteSum(s1,s2)
# answer
answer = 403
print(output, answer, answer == output)
