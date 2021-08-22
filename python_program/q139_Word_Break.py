from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_len_dict = defaultdict(set)
        for word in wordDict:
            word_len_dict[len(word)].add(word)

        dp = [False]*(n+1)
        dp[0]=True
        
        for i in range(1,n+1):
            for k in word_len_dict.keys():
                if i-k>=0 and dp[i-k] and s[i-k:i] in word_len_dict[k]:
                    dp[i]= True
        return dp[n]

sol = Solution()


# input
s = "leetcode"
wordDict = ["leet","code"]
# output
output = sol.wordBreak(s,wordDict)
# answer
answer = True
print(output, answer, answer == output)

# input
s = "applepenapple"
wordDict = ["apple","pen"]

# output
output = sol.wordBreak(s,wordDict)
# answer
answer = True
print(output, answer, answer == output)

# input
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
# output
output = sol.wordBreak(s,wordDict)
# answer
answer = False
print(output, answer, answer == output)
