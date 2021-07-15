from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        s_n = len(s)
        t_n = len(t)
        min_n = min(s_n,t_n)
        s_count_substring = [defaultdict(int) for _ in range(s_n+1)]         
        t_count_substring = [defaultdict(int) for _ in range(t_n+1)]
        
        def diff_by_one(x,y):
            count = 0
            for i,j in zip(x,y):
                if i!=j:
                    count+=1
                if count>=2:
                    return False
            if count ==1:
                return True
            else:
                return False
            
        for i in range(min_n):
            for j in range(i,s_n):
                s_count_substring[i+1][s[(j-i):j+1]]+=1
        for i in range(min_n):
            for j in range(i,t_n):                
                t_count_substring[i+1][t[(j-i):j+1]]+=1

        count = 0
        for i in range(min_n):
            for x in s_count_substring[i+1]:
                for y in t_count_substring[i+1]:
                    if diff_by_one(x,y):
                        count += s_count_substring[i+1][x]*t_count_substring[i+1][y]
        return count

sol = Solution()


# input
s = "aba"

t = "baba"

# output
output = sol.countSubstrings(s,t)
# answer
answer = 6
print(output, answer, answer == output)

# input
s = "ab"

t = "bb"

# output
output = sol.countSubstrings(s,t)
# answer
answer = 3
print(output, answer, answer == output)

# input
s = "a"

t = "a"

# output
output = sol.countSubstrings(s,t)
# answer
answer = 0
print(output, answer, answer == output)

# input
s = "abe"

t = "bbc"

# output
output = sol.countSubstrings(s,t)
# answer
answer = 10
print(output, answer, answer == output)
