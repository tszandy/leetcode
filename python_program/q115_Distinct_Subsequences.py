from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def numDistinct(self, s: str, t: str) -> int:    
        n_s = len(s)
        n_t = len(t)

        @lru_cache(None)
        def dp(i=0,j=0):
            if j == n_t:
                return 1
            if i == n_s:
                return 0
            if s[i] == t[j]:
                return dp(i+1,j+1)+dp(i+1,j)
            else:
                return dp(i+1,j)
        return dp()




    def numDistinct_3(self, s: str, t: str) -> int:    
        n_s = len(s)
        n_t = len(t)
        
        s_char_to_index = defaultdict(list)
        for i,e in enumerate(s):
            s_char_to_index[e].append(i)

        t_char_to_index = defaultdict(list)
        for i,e in enumerate(t):
            t_char_to_index[e].append(i)

        t_char_to_pre_char = defaultdict(list)
        for i in range(1,len(t))[::-1]:
            t_char_to_pre_char[t[i]].append(t[i-1])
                
        dp = [defaultdict(int) for _ in range(n_s)]
        for j in range(n_s):
            e_2 = s[j]
            if e_2 == t[0]:
                dp[j][0]=1
            for index in t_char_to_index[e_2]:
                for pre_char in t_char_to_pre_char[e_2]:
                    for i in s_char_to_index[pre_char]:
                        if i <j:
                            dp[j][index]+=dp[i][index-1]
        count = 0
        for i in s_char_to_index[t[-1]]:
            count+=dp[i][n_t-1]
        return count

#backtracking time limit exceeded
    def numDistinct_2(self, s: str, t: str) -> int:
        n_s = len(s)
        n_t = len(t)

        count = [0]
        def backtracking(s_index,t_index):
            if t_index == n_t:
                count[0]+=1
                return
            if s_index>=n_s:
                return
            if s[s_index]==t[t_index]:
                backtracking(s_index+1,t_index+1)
            backtracking(s_index+1,t_index)

        backtracking(0,0)
        return count[0]




# char in t not distinct, there is a problem in this program
    def numDistinct_1(self, s: str, t: str) -> int:
        t_char_to_index = defaultdict(list)
        for i,e in enumerate(t):
            t_char_to_index[e].append(i)
        t_char_to_pre_char = {}
        for i in range(1,len(t))[::-1]:
            t_char_to_pre_char[t[i]] = t[i-1]
            
        s_char_to_index = defaultdict(list)
        for i,e in enumerate(t):
            s_char_to_index[e].append(i)
        
        print(t_char_to_pre_char)
        
        n = len(s)
        dp = defaultdict(int)
        for j in range(n):
            e_2 = s[j]
            if e_2 == t[0]:
                dp[j]=1
            for i in s_char_to_index[t_char_to_pre_char[e_2]]:
                if i <j:
                    dp[j]+=dp[i]
        count = 0
        for i in s_char_to_index[t[-1]]:
            count+=dp[i]
        return count

sol = Solution()


# input
s = "rabbbit"

t = "rabbit"

# output
output = sol.numDistinct(s,t)
# answer
answer = 3
print(output, answer, answer == output)

# input
s = "rrarrabababaitbbit"

t = "rrabbit"

# output
output = sol.numDistinct(s,t)
# answer
answer = 184
print(output, answer, answer == output)

# input
s = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"

t = "bddab"

# output
output = sol.numDistinct(s,t)
# answer
answer = 56043
print(output, answer, answer == output)

# input
s = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"

t = "bddabd"

# output
output = sol.numDistinct(s,t)
# answer
answer = 167894
print(output, answer, answer == output)

# input
s = "babgbag"

t = "bag"

# output
output = sol.numDistinct(s,t)
# answer
answer = 5
print(output, answer, answer == output)

# input
s = "abgbag"

t = "bag"

# output
output = sol.numDistinct(s,t)
# answer
answer = 2
print(output, answer, answer == output)

# input
s = "ababgbabag"

t = "bag"

# output
output = sol.numDistinct(s,t)
# answer
answer = 9
print(output, answer, answer == output)

# input
s = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"

t = "bddabdcae"

# output
output = sol.numDistinct(s,t)
# answer
answer = 10582116
print(output, answer, answer == output)
