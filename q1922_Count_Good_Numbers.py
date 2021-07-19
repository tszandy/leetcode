from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def __init__(self):
        self.mod_num = 10**9+7
    def countGoodNumbers(self, n: int) -> int:
        return (self.fast_power_mod(20,n//2)*5**(n%2))%(self.mod_num)

    def fast_power_mod(self,a,n):
        if n ==0:
            return 1
        if n ==1:
            return a
        if n %2 == 1:
            return (a*self.fast_power_mod((a**2)%self.mod_num,n//2))%self.mod_num
        else:
            return (self.fast_power_mod((a**2)%self.mod_num,n//2))%self.mod_num

sol = Solution()


# input
n = 1

# output
output = sol.countGoodNumbers(n)
# answer
answer = 5
print(output, answer, answer == output)

# input
n = 4

# output
output = sol.countGoodNumbers(n)
# answer
answer = 400
print(output, answer, answer == output)

# input
n = 50

# output
output = sol.countGoodNumbers(n)
# answer
answer = 564908303
print(output, answer, answer == output)

# input
n = 1000000000000000

# output
output = sol.countGoodNumbers(n)
# answer
answer = 711414395
print(output, answer, answer == output)
