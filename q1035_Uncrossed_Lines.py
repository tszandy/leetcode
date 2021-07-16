from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n_1 = len(nums1)
        n_2 = len(nums2)
        @lru_cache(None)
        def dp(nums_1_r,nums_2_r):
            if nums_1_r==0 or nums_2_r==0:
                return 0
            
            break_for_loop_1 = False
            store_nums_1_index_1 = None
            store_nums_2_index_1 = None
            for i in range(nums_1_r)[::-1]:
                for j in range(nums_2_r)[::-1]:
                    if nums1[i]==nums2[j]:
                        store_nums_1_index_1 = i
                        store_nums_2_index_1 = j
                        break_for_loop_1 = True
                    if break_for_loop_1:
                        break
                if break_for_loop_1:
                    break
            if not break_for_loop_1:
                return 0
                    
            break_for_loop_2 = False
            store_nums_1_index_2 = None
            store_nums_2_index_2 = None
            for i in range(nums_2_r)[::-1]:
                for j in range(nums_1_r)[::-1]:
                    if nums2[i]==nums1[j]:
                        store_nums_1_index_2 = j
                        store_nums_2_index_2 = i
                        break_for_loop_2 = True
                    if break_for_loop_2:
                        break
                if break_for_loop_2:
                    break

            if store_nums_1_index_1 == store_nums_1_index_2:
                return 1+dp(store_nums_1_index_1,store_nums_2_index_1)
            else:
                sub_ans_1 = 1+dp(store_nums_1_index_1,store_nums_2_index_1)
                sub_ans_2 = 1+dp(store_nums_1_index_2,store_nums_2_index_2)
                sub_ans_3 = dp(store_nums_1_index_1,store_nums_2_index_2)
                return max(sub_ans_1,sub_ans_2,sub_ans_3)
        return dp(n_1,n_2)
sol = Solution()


# input
nums1 = [1,4,2]

nums2 = [1,2,4]

# output
output = sol.maxUncrossedLines(nums1,nums2)
# answer
answer = 2
print(output, answer, answer == output)

# input
nums1 = [2,5,1,2,5]

nums2 = [10,5,2,1,5,2]

# output
output = sol.maxUncrossedLines(nums1,nums2)
# answer
answer = 3
print(output, answer, answer == output)

# input
nums1 = [1,3,7,1,7,5]

nums2 = [1,9,2,5,1]

# output
output = sol.maxUncrossedLines(nums1,nums2)
# answer
answer = 2
print(output, answer, answer == output)

# input
nums1 = [1,3,7,1,7,5,1,3,7,1,7,5,1,3,7,1,7,5,1,3,7,1,7,5]

nums2 = [1,9,2,5,1,1,9,2,5,1,1,9,2,5,1,1,9,2,5,1,1,9,2,5,1,1,9,2,5,1,1,9,2,5,1,1,9,2,5,1]

# output
output = sol.maxUncrossedLines(nums1,nums2)
# answer
answer = 12
print(output, answer, answer == output)

# input
nums1 = [4,1,2,5,1,5,3,4,1,5]

nums2 = [3,1,1,3,2,5,2,4,1,3,2,2,5,5,3,5,5,1,2,1]

# output
output = sol.maxUncrossedLines(nums1,nums2)
# answer
answer = 7
print(output, answer, answer == output)
