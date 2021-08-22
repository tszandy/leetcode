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
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts)

sol = Solution()

# input
accounts = [[1,2,3],[3,2,1]]

# output
output = sol.maximumWealth(accounts)
# answer
answer = 6
print(output, answer, answer == output)

# input
accounts = [[1,5],[7,3],[3,5]]

# output
output = sol.maximumWealth(accounts)
# answer
answer = 10
print(output, answer, answer == output)

# input
accounts = [[2,8,7],[7,1,3],[1,9,5]]

# output
output = sol.maximumWealth(accounts)
# answer
answer = 17
print(output, answer, answer == output)
