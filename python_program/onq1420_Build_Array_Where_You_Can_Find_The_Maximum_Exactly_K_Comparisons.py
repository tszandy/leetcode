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
    @lru_cache(None)
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k == 0:
            return 0
        if k>m or k>n:
            return 0
        if m == 1 and k == 1:
            return 1
        if n == 1 and k == 1:
            return m % 1000000007
        if k == 1:
            result = 0
            for i in range(1,m+1):
                result += self.numOfArrays(n-1,i,1)
            return result % 1000000007
        result = self.numOfArrays(n-1,m,k)+self.numOfArrays(n,m-1,k)+self.numOfArrays(n,m-1,k-1)
        return result % 1000000007

sol = Solution()

# input

# output
output = sol.numOfArrays(n,m,k)
# answer
answer = ""

print(output, answer, answer == output)

