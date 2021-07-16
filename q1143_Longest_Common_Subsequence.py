from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def longestCommonSubsequence_1(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp =defaultdict(list)
        dp[(-1,-1)]=0
        
        for i in range(m):
            c1 = text1[i]
            for j in range(n):
                c2 = text2[j]
                if c1 == c2:
                    if i==0 or j ==0 :
                        dp[(i,j)]=(1,None)
                    else:
                        max_sub = 0
                        index = (0,0)
                        for ii in range(i):
                        	cur_sub = dp[(ii,j-1)]+1
                        	if cur_sub > max_sub:
                        		max_sub = cur_sub
                        		index = ii,j-1
                        dp[(i,j)].append((max_sub,index))
        return max(dp.values())

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
