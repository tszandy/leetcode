from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if k == 1:
            return (self.largest_subarr_sum(arr))% (10**9 + 7)
        k_2_sum = self.largest_subarr_sum(arr+arr)
        if k == 2:
            return k_2_sum % (10**9 + 7)
        arr_sum = sum(arr)
        if arr_sum >0:
            return (k_2_sum+arr_sum*(k-2))% (10**9 + 7)
        else:
            return k_2_sum % (10**9 + 7)
    
    def largest_subarr_sum(self, arr):
        max_sum = arr[0]
        subarr_sum = 0
        n = len(arr)
        for i in range(n):
            subarr_sum += arr[i]
            if subarr_sum < 0:
                subarr_sum = 0
            max_sum = max(max_sum,subarr_sum)
        return max_sum

sol = Solution()


# input
arr = [-1]
k = 1
# output
output = sol.kConcatenationMaxSum(arr,k)
# answer
answer = 0
print(output, answer, answer == output)

# input
arr = [1,2]
k = 3
# output
output = sol.kConcatenationMaxSum(arr,k)
# answer
answer = 9
print(output, answer, answer == output)

# input
arr = [1,-2,1]
k = 5
# output
output = sol.kConcatenationMaxSum(arr,k)
# answer
answer = 2
print(output, answer, answer == output)

# input
arr = [-1,-2]
k = 7
# output
output = sol.kConcatenationMaxSum(arr,k)
# answer
answer = 0
print(output, answer, answer == output)

# input
arr = [-9,4,5,6,1,2,-10]
k = 7
# output
output = sol.kConcatenationMaxSum(arr,k)
# answer
answer = 18
print(output, answer, answer == output)

# input
arr = [-9,4,5,6,1,2]
k = 7
# output
output = sol.kConcatenationMaxSum(arr,k)
# answer
answer = 72
print(output, answer, answer == output)

# input
arr = [-9,4,5,6,1,2]
k = 1
# output
output = sol.kConcatenationMaxSum(arr,k)
# answer
answer = 18
print(output, answer, answer == output)

# input
arr = [-9,4,5,6,1,2]
k = 2
# output
output = sol.kConcatenationMaxSum(arr,k)
# answer
answer = 27
print(output, answer, answer == output)

# input
arr = [10000,10000,10000,10000,10000,10000,10000,10000,10000,10000]
k = 100000
# output
output = sol.kConcatenationMaxSum(arr,k)
# answer
answer = 999999937
print(output, answer, answer == output)
