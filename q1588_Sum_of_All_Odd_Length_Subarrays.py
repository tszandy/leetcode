from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        count = 0
        n = len(arr)
        for i in range(1,n+1,2):
            for j in range(i-1,n):
                count+=sum(arr[j-i+1:j+1])
        return count

sol = Solution()


# input
arr = [1,4,2,5,3]

# output
output = sol.sumOddLengthSubarrays(arr)
# answer
answer = 58
print(output, answer, answer == output)

# input
arr = [1,2]

# output
output = sol.sumOddLengthSubarrays(arr)
# answer
answer = 3
print(output, answer, answer == output)

# input
arr = [1]

# output
output = sol.sumOddLengthSubarrays(arr)
# answer
answer = 1
print(output, answer, answer == output)

# input
arr = [10,11,12]

# output
output = sol.sumOddLengthSubarrays(arr)
# answer
answer = 66
print(output, answer, answer == output)

# input
arr = [10,11,12,10,11,12,10,11,12,10,11,12,10,11,12,10,11,12,10,11,12,10,11,12,10,11,12,10,11,12,10,11,12,10,11,12,10,11,12,10,11,12,10,11,12,10,11,12,10,11,12]

# output
output = sol.sumOddLengthSubarrays(arr)
# answer
answer = 128986
print(output, answer, answer == output)
