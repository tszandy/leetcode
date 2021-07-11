from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n ==1 and len(trust)==0:
            return 1
        store_truster = set()
        store_set_b_to_a = defaultdict(set)
        
        for (a,b) in trust:
            store_truster.add(a)
            store_set_b_to_a[b].add(a)
        
        for key in store_set_b_to_a:
            if len(store_set_b_to_a[key])==n-1 and key not in store_truster:
                return key
        return -1

sol = Solution()


# input
n = 2

trust = [[1,2]]

# output
output = sol.findJudge(n,trust)
# answer
answer = 2
print(output, answer, answer == output)

# input
n = 3

trust = [[1,3],[2,3]]

# output
output = sol.findJudge(n,trust)
# answer
answer = 3
print(output, answer, answer == output)

# input
n = 3

trust = [[1,3],[2,3],[3,1]]

# output
output = sol.findJudge(n,trust)
# answer
answer = -1
print(output, answer, answer == output)

# input
n = 3

trust = [[1,2],[2,3]]

# output
output = sol.findJudge(n,trust)
# answer
answer = -1
print(output, answer, answer == output)

# input
n = 4

trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]

# output
output = sol.findJudge(n,trust)
# answer
answer = 3
print(output, answer, answer == output)

# input
n = 1

trust = []

# output
output = sol.findJudge(n,trust)
# answer
answer = 1
print(output, answer, answer == output)
