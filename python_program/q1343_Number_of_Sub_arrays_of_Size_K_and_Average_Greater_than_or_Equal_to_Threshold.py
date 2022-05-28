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
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        arr_len = len(arr)
        threshold *=k
        arr_sum = 0
        if not k==1:
            arr_sum = reduce(lambda x,y:x+y,arr[:k-1])
        return_val = 0
        for i in range(k-1,arr_len):
            arr_sum += arr[i]
            if arr_sum >= threshold:
                return_val +=1
            arr_sum -= arr[i-k+1]
        return return_val

sol = Solution()

# input
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
# output
output = sol.numOfSubarrays(arr,k,threshold)
# answer
answer = 3
print(output, answer, answer == output)

# input
arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5
# output
output = sol.numOfSubarrays(arr,k,threshold)
# answer
answer = 6
print(output, answer, answer == output)

# input
arr = [11,13,17,23,29,31,7,5,1,2,3,4,1,2,1,5,1,2,12,32,5,2,100,2,3]
k = 3
threshold = 5
# output
output = sol.numOfSubarrays(arr,k,threshold)
# answer
answer = 13
print(output, answer, answer == output)

# input
arr = [11,13,17,23,29,31,7,5,1,2,3,4,1,2,1,5,1,2,12,32,5,2,100,2,3]
k = 5
threshold = 7
# output
output = sol.numOfSubarrays(arr,k,threshold)
# answer
answer = 12
print(output, answer, answer == output)

# input
arr = [11]
k = 1
threshold = 7
# output
output = sol.numOfSubarrays(arr,k,threshold)
# answer
answer = 1
print(output, answer, answer == output)

# input
arr = [11,3]
k = 2
threshold = 7
# output
output = sol.numOfSubarrays(arr,k,threshold)
# answer
answer = 1
print(output, answer, answer == output)

# input
arr = [1,1,1,1,1]
k = 1
threshold = 0
# output
output = sol.numOfSubarrays(arr,k,threshold)
# answer
answer = 1
print(output, answer, answer == output)
