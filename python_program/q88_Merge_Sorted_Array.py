from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r_merge_list = m+n-1
        r_nums1 = m-1
        r_nums2 = n-1
        while 0<=r_nums2 and 0<=r_nums1:
            if nums1[r_nums1]<=nums2[r_nums2]:
                nums1[r_merge_list] = nums2[r_nums2]
                r_merge_list-=1
                r_nums2-=1
            else:
                nums1[r_merge_list] = nums1[r_nums1]
                r_merge_list-=1
                r_nums1-=1
        if r_nums1<0:
            for i in range(r_nums2+1):
                nums1[i]=nums2[i]
        return nums1

sol = Solution()

# input
nums1 = [1,2,3,0,0,0]

m = 3

nums2 = [2,5,6]

n = 3

# output
output = sol.merge(nums1,m,nums2,n)
# answer
answer = [1,2,2,3,5,6]

print(output, answer, answer == output)

# input
nums1 = [1]

m = 1

nums2 = []

n = 0

# output
output = sol.merge(nums1,m,nums2,n)
# answer
answer = [1]

print(output, answer, answer == output)

# input
nums1 = [0]

m = 0

nums2 = [1]

n = 1

# output
output = sol.merge(nums1,m,nums2,n)
# answer
answer = [1]

print(output, answer, answer == output)

# input
nums1 = [2,0]

m = 1

nums2 = [1]

n = 1

# output
output = sol.merge(nums1,m,nums2,n)
# answer
answer = [1,2]

print(output, answer, answer == output)
