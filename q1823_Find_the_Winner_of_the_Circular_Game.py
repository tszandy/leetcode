from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = None
        cur = -1
        mod_num = n
        player_list = list(range(1,n+1))
        while player_list:
            cur = (cur+k)%mod_num
            winner = player_list.pop(cur)
            cur -=1
            mod_num-=1
        return winner

sol = Solution()


# input
n = 5

k = 2

# output
output = sol.findTheWinner(n,k)
# answer
answer = 3
print(output, answer, answer == output)

# input
n = 6

k = 1

# output
output = sol.findTheWinner(n,k)
# answer
answer = 6
print(output, answer, answer == output)

# input
n = 6

k = 2

# output
output = sol.findTheWinner(n,k)
# answer
answer = 5
print(output, answer, answer == output)

# input
n = 6

k = 3

# output
output = sol.findTheWinner(n,k)
# answer
answer = 1
print(output, answer, answer == output)

# input
n = 6

k = 5

# output
output = sol.findTheWinner(n,k)
# answer
answer = 1
print(output, answer, answer == output)

# input
n = 500

k = 79

# output
output = sol.findTheWinner(n,k)
# answer
answer = 1
print(output, answer, answer == output)
