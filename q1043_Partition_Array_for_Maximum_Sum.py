from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        store_max_sum_score = [defaultdict(int) for _ in range(n)]
        store_max_elem = defaultdict(int)
        store_max_sum_score[0][0]=arr[0]
        store_max_sum_score[0][1]=0
        store_max_elem[(0,1)]=arr[0]
        
        for i in range(1,n):
            for k_index in store_max_sum_score[i-1]:
                if k_index<k:
                    store_max_sum_score[i][k_index+1] = store_max_sum_score[i-1][k_index]
                    store_max_elem[(i,k_index+1)] = max(store_max_elem[(i-1,k_index)],arr[i])
            
            max_score = 0
            for k_index in store_max_sum_score[i]:
                max_score = max(max_score,store_max_sum_score[i][k_index]+store_max_elem[(i,k_index)]*k_index)
            store_max_sum_score[i][0] = max_score
            store_max_elem[(i,0)]=0
        return store_max_sum_score[n-1][0]

sol = Solution()


# input
arr = [1,15,7,9,2,5,10]

k = 3

# output
output = sol.maxSumAfterPartitioning(arr,k)
# answer
answer = 84
print(output, answer, answer == output)

# input
arr = [1,4,1,5,7,3,6,1,9,9,3]

k = 4

# output
output = sol.maxSumAfterPartitioning(arr,k)
# answer
answer = 83
print(output, answer, answer == output)

# input
arr = [1]

k = 1

# output
output = sol.maxSumAfterPartitioning(arr,k)
# answer
answer = 1
print(output, answer, answer == output)

# input
arr = [1,2]

k = 2

# output
output = sol.maxSumAfterPartitioning(arr,k)
# answer
answer = 4
print(output, answer, answer == output)

# input
arr = [1,2,3,4,5,1,2,3]

k = 1

# output
output = sol.maxSumAfterPartitioning(arr,k)
# answer
answer = 21
print(output, answer, answer == output)

# input
arr = [1,2,3,4,5,1,2,3]

k = 2

# output
output = sol.maxSumAfterPartitioning(arr,k)
# answer
answer = 28
print(output, answer, answer == output)
