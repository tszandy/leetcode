from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
#backtracking runtime expential
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        sum_match_stick = sum(matchsticks)
        if sum_match_stick %4!=0:
            return False
        side_length = sum_match_stick//4
        
        matchsticks.sort(reverse=True)
        
        sums = [0 for _ in range(4)]
        
        def backtracking(index):
            if index == n:
                return sums[0] == sums[1] == sums[2] == side_length
        
            for i in range(4):
                if sums[i] + matchsticks[index] <= side_length:
                    sums[i] += matchsticks[index]
                    if backtracking(index+1):
                        return True
                    sums[i]-=matchsticks[index]
            return False
        return backtracking(0)
                                        

sol = Solution()

# input
matchsticks = [1,1,2,2,2]

# output
output = sol.makesquare(matchsticks)
# answer
answer = True
print(output, answer, answer == output)

# input
matchsticks = [3,3,3,3,4]

# output
output = sol.makesquare(matchsticks)
# answer
answer = False
print(output, answer, answer == output)
