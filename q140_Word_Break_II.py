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
        dp_list = defaultdict(list)
        
        for i in range(1,n+1):
            for k in word_len_dict.keys():
                if i-k>=0 and dp[i-k] and s[i-k:i] in word_len_dict[k]:
                    dp[i]= True
                    dp_list[i].append(s[i-k:i])
        return_list = []
        
        def backtracking(n, string_list):
            if n == 0:
                return_list.append(" ".join(string_list[::-1]))
            for word in dp_list[n]:
                string_list.append(word)
                backtracking(n-len(word),string_list)
                string_list.pop()
                
        
        if dp[n]:
            backtracking(n,[])            
        return return_list
        

sol = Solution()


# input
s = "catsanddog"

wordDict = ["cat","cats","and","sand","dog"]

# output
output = sol.wordBreak(s,wordDict)
# answer
answer = ["cats and dog","cat sand dog"]
print(output, answer, answer == output)

# input
s = "pineapplepenapple"

wordDict = ["apple","pen","applepen","pine","pineapple"]

 # output
output = sol.wordBreak(s,wordDict)
# answer
answer = ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
print(output, answer, answer == output)

# input
s = "catsandog"

wordDict = ["cats","dog","sand","and","cat"]

# output
output = sol.wordBreak(s,wordDict)
# answer
answer = []
print(output, answer, answer == output)
