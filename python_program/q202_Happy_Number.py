from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count
import queue

class Solution:
    def isHappy(self, n: int) -> bool:
        self.store_set = set()
        return self.is_happy(n)
        
    def is_happy(self,n):
        if n == 1 :
            return True
        num = sum(map(lambda x:int(x)**2,str(n)))
        if num in self.store_set:
            return False
        else:
            self.store_set.add(num)
            return self.is_happy(num)

sol = Solution()

# input
n = 2147483647

# output
output = sol.isHappy(n)
# answer
answer = False
print(output, answer, answer == output)

# input
n = 19

# output
output = sol.isHappy(n)
# answer
answer = True
print(output, answer, answer == output)

# input
n = 2

# output
output = sol.isHappy(n)
# answer
answer = False
print(output, answer, answer == output)
