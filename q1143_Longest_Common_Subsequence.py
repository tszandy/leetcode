from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp =defaultdict(int)
        dp[(-1,-1)]=0
        
        for i in range(m):
            c1 = text1[i]
            for j in range(n):
                c2 = text2[j]
                if c1==c2:
                    dp[(i,j)] = dp[(i-1,j-1)]+1
                else:
                    dp[(i,j)] = max(dp[(i-1,j)],dp[(i,j-1)])
            
        return max(dp.values())


sol = Solution()


# input
text1 = "abcde"

text2 = "ace" 

# output
output = sol.longestCommonSubsequence(text1,text2)
# answer
answer = 3
print(output, answer, answer == output)

# input
text1 = "abc"

text2 = "abc"

# output
output = sol.longestCommonSubsequence(text1,text2)
# answer
answer = 3
print(output, answer, answer == output)

# input
text1 = "abc"

text2 = "def"

# output
output = sol.longestCommonSubsequence(text1,text2)
# answer
answer = 0
print(output, answer, answer == output)

# input
text1 = "ezupkr"

text2 = "ubmrapg"

# output
output = sol.longestCommonSubsequence(text1,text2)
# answer
answer = 2
print(output, answer, answer == output)
