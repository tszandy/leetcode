from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def rotatedDigits(self, n: int) -> int:
        rotate_set = set(['0','1','8','2','5','6','9'])
        rotate_to_each_other_set = set(['2','5','6','9'])
        
        count = 0
        for i in range(2,n+1):
            rotate_able = False
            for d in str(i):
                if d not in rotate_set:
                    rotate_able = False
                    break
                if d in rotate_to_each_other_set:
                    rotate_able = True
            if rotate_able:
                count+=1
        return count

sol = Solution()


# input
n = 1
# output
output = sol.rotatedDigits(n)
# answer
answer = 0
print(output, answer, answer == output)

# input
n = 2
# output
output = sol.rotatedDigits(n)
# answer
answer = 1
print(output, answer, answer == output)

# input
n = 10
# output
output = sol.rotatedDigits(n)
# answer
answer = 4
print(output, answer, answer == output)

# input
n = 9999
# output
output = sol.rotatedDigits(n)
# answer
answer = 2320
print(output, answer, answer == output)
