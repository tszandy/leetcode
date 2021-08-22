from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
import heapq

class MaxHeap:
    def __init__(self,data):
        self.data = list(map(lambda x:-x,data))
        heapq.heapify(self.data)

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)
        

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        n = len(target)
        total_sum = sum(target)
        max_heap = MaxHeap(target)
        
        elem = max_heap.pop()
        total_sum_wo_elem = total_sum-elem
        before_sum_elem = elem-total_sum_wo_elem
        total_sum = before_sum_elem + total_sum_wo_elem
        if before_sum_elem<1 and sum(max_heap.data) == n-1 and elem ==1:
            return True
        max_heap.push(before_sum_elem)
        while before_sum_elem>=1:
            elem = max_heap.pop()
            total_sum_wo_elem = total_sum-elem
            before_sum_elem = elem-total_sum_wo_elem
            total_sum = before_sum_elem + total_sum_wo_elem
            if before_sum_elem<1 and sum(max_heap.data) == -(n-1) and elem ==1:
                return True
            max_heap.push(before_sum_elem)
        return False

sol = Solution()


# input
target = [9,3,5]
# output
output = sol.isPossible(target)
# answer
answer = True
print(output, answer, answer == output)

# input
target = [1,1,1,2]
# output
output = sol.isPossible(target)
# answer
answer = False
print(output, answer, answer == output)

# input
target = [8,5]
# output
output = sol.isPossible(target)
# answer
answer = True
print(output, answer, answer == output)
