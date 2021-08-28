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
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(1,n)[::-1]:
            pre_num = arr[i-1]
            cur_num = arr[i]
            if pre_num>cur_num:
                swap_elem_1 = pre_num
                swap_index_1 = i-1
                swap_elem_2 = cur_num
                swap_index_2 = i
                for j in range(i,n):
                    if swap_elem_2<arr[j]<swap_elem_1:
                        swap_elem_2 = arr[j]
                        swap_index_2 = j
                arr[swap_index_1],arr[swap_index_2]=arr[swap_index_2],arr[swap_index_1]
                break
        return arr

sol = Solution()

# input
arr = [3,2,1]

# output
output = sol.prevPermOpt1(arr)
# answer
answer = [3,1,2]

print(output, answer, answer == output)

# input
arr = [1,1,5]

# output
output = sol.prevPermOpt1(arr)
# answer
answer = [1,1,5]

print(output, answer, answer == output)

# input
arr = [1,9,4,6,7]

# output
output = sol.prevPermOpt1(arr)
# answer
answer = [1,7,4,6,9]

print(output, answer, answer == output)

# input
arr = [3,1,1,3]

# output
output = sol.prevPermOpt1(arr)
# answer
answer = [1,3,1,3]

print(output, answer, answer == output)
