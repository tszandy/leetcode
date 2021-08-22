from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)
        count_zero = list(map(lambda x:sum(map(lambda y:1-int(y),x)),strs))
        count_one  = list(map(lambda x:sum(map(lambda y:int(y),x)),strs))

        dp = [[0]*(n+1) for _ in range(m+1)]
        
        visited_set = set()
        for i in range(l):
            x_2,y_2 = count_zero[i],count_one[i]
            need_change = []
            if x_2<=m and y_2<=n:
                need_change.append((x_2,y_2,max(dp[x_2][y_2],1)))
            add_to_visited_set = []
            for (x_1,y_1) in visited_set:
                if x_1+x_2<=m and y_1+y_2<=n:
                    need_change.append((x_1+x_2,y_1+y_2,max(dp[x_1+x_2][y_1+y_2],dp[x_1][y_1]+1)))
                    add_to_visited_set.append((x_1+x_2,y_1+y_2))
            if x_2<=m and y_2<=n:
                visited_set.add((x_2,y_2))
            for x,y in add_to_visited_set:
                visited_set.add((x,y))
            for x,y,delta in need_change:
                dp[x][y]=delta
        return max(max(b for b in a)for a in dp)
            

sol = Solution()

# input
strs = ["10","0001","111001","1","0"]
m = 5
n = 3
# output
output = sol.findMaxForm(strs,m,n)
# answer
answer = 4
print(output, answer, answer == output)

# input
strs = ["10","0","1"]
m = 1
n = 1
# output
output = sol.findMaxForm(strs,m,n)
# answer
answer = 2
print(output, answer, answer == output)

# input
strs = ["10","0001","111001","1","0","10","0001","111001","1","0","10","0001","111001","1","0","10","0001","111001","1","0","10","0001","111001","1","0"]
m = 9
n = 5
# output
output = sol.findMaxForm(strs,m,n)
# answer
answer = 10
print(output, answer, answer == output)
