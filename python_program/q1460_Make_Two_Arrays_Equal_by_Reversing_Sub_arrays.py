from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        return target == arr

sol = Solution()


# input
target = [1,2,3,4]

arr = [2,4,1,3]

# output
output = sol.canBeEqual(target,arr)
# answer
answer = True
print(output, answer, answer == output)

# input
target = [7]

arr = [7]

# output
output = sol.canBeEqual(target,arr)
# answer
answer = True
print(output, answer, answer == output)

# input
target = [1,12]

arr = [12,1]

# output
output = sol.canBeEqual(target,arr)
# answer
answer = True
print(output, answer, answer == output)

# input
target = [3,7,9]

arr = [3,7,11]

# output
output = sol.canBeEqual(target,arr)
# answer
answer = False
print(output, answer, answer == output)

# input
target = [1,1,1,1,1]

arr = [1,1,1,1,1]

# output
output = sol.canBeEqual(target,arr)
# answer
answer = True
print(output, answer, answer == output)