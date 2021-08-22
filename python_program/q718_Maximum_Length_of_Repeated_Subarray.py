from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if nums1[i]==nums2[j]:
                    if i!=0 and j !=0:
                        dp[i][j] = dp[i-1][j-1]+1
                    else:
                        dp[i][j] = 1
        
        return max(max(row) for row in dp)

sol = Solution()


# input
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
# output
output = sol.findLength(nums1,nums2)
# answer
answer = 3
print(output, answer, answer == output)

# input
nums1 = [0,0,0,0,0]
nums2 = [0,0,0,0,0]
# output
output = sol.findLength(nums1,nums2)
# answer
answer = 5
print(output, answer, answer == output)

# input
nums1 = [1]
nums2 = [2]
# output
output = sol.findLength(nums1,nums2)
# answer
answer = 0
print(output, answer, answer == output)
