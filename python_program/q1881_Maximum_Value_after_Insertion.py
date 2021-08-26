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
    def maxValue(self, n: str, x: int) -> str:
        length = len(n)
        n = int(n)
        if n<0:
            nums = list(str(abs(n)))
            for i in range(len(nums)):
                if int(nums[i])>x:
                    nums.insert(i,str(x))
                    break
            result = "-"+"".join(nums)
        else:
            nums = list(str(abs(n)))
            for i in range(len(nums)):
                if int(nums[i])<x:
                    nums.insert(i,str(x))
                    break
            result = "".join(nums)
        if len(result) == length:
            return result+str(x)
        else:
            return result

sol = Solution()

# input
n = "99"

x = 9

# output
output = sol.maxValue(n,x)
# answer
answer = "999"
print(output, answer, answer == output)

# input
n = "-13"

x = 2

# output
output = sol.maxValue(n,x)
# answer
answer = "-123"
print(output, answer, answer == output)

# input
n = "-31"

x = 2

# output
output = sol.maxValue(n,x)
# answer
answer = "-231"
print(output, answer, answer == output)

# input
n = "13"

x = 2

# output
output = sol.maxValue(n,x)
# answer
answer = "213"
print(output, answer, answer == output)

# input
n = "-132"

x = 3

# output
output = sol.maxValue(n,x)
# answer
answer = "-1323"
print(output, answer, answer == output)

# input
n = "32"

x = 1

# output
output = sol.maxValue(n,x)
# answer
answer = "321"
print(output, answer, answer == output)

# input
n = "469975787943862651173569913153377"

x = 3

# output
output = sol.maxValue(n,x)
# answer
answer = "4699757879438632651173569913153377"
print(output, answer, answer == output)
