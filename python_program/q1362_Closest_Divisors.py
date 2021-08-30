from typing import List
from collections import Counter,defaultdict,deque
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count,zip_longest
import queue

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        factor_1 = self.factor(num+1)
        factor_2 = self.factor(num+2)
        
        return factor_1 if abs(factor_1[0]-factor_1[1])<abs(factor_2[0]-factor_2[1])else factor_2
        
    def factor(self,num):
        for i in range(1,int(sqrt(num))+1)[::-1]:
            if num%i==0:
                return [i,num//i]


sol = Solution()

# input
num = 8

# output
output = sol.closestDivisors(num)
# answer
answer = [3,3]

print(output, answer, answer == output)

# input
num = 123

# output
output = sol.closestDivisors(num)
# answer
answer = [5,25]

print(output, answer, answer == output)

# input
num = 999

# output
output = sol.closestDivisors(num)
# answer
answer = [25,40]

print(output, answer, answer == output)
