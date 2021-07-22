from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n_w1 = len(word1)
        n_w2 = len(word2)
        return n_w1+n_w2-self.longestCommonSubsequence(word1,word2)*2
    
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
word1 = "sea"

word2 = "eat"

# output
output = sol.minDistance(word1,word2)
# answer
answer = 2
print(output, answer, answer == output)

# input
word1 = "leetcode"

word2 = "etco"

# output
output = sol.minDistance(word1,word2)
# answer
answer = 4
print(output, answer, answer == output)
