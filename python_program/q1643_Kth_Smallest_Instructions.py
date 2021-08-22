from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
# backtracking, pass 5/462 test
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        self.iterator_counter = count(1)
        self.destination = destination
        self.k = k
        return "".join(self.backtracking(0,0,[]))
        
    def backtracking(self,count_h,count_v,store_list):
        if count_h>self.destination[1] or count_v>self.destination[0]:
            return
        if count_h ==self.destination[1] and count_v == self.destination[0] and next(self.iterator_counter)==self.k:
            return store_list
        
        result = self.backtracking(count_h+1,count_v,store_list+["H"])
        if result != None:
            return result
        result = self.backtracking(count_h,count_v+1,store_list+["V"]) 
        if result != None:
            return result
        return

sol = Solution()

# input
destination = [2,3]

k = 1

# output
output = sol.kthSmallestPath(destination,k)
# answer
answer = "HHHVV"
print(output, answer, answer == output)

# input
destination = [2,3]

k = 2

# output
output = sol.kthSmallestPath(destination,k)
# answer
answer = "HHVHV"
print(output, answer, answer == output)

# input
destination = [2,3]

k = 3

# output
output = sol.kthSmallestPath(destination,k)
# answer
answer = "HHVVH"
print(output, answer, answer == output)

# input
destination = [15,15]

k = 30

# output
output = sol.kthSmallestPath(destination,k)
# answer
answer = "HHHHHHHHHHHHHVHVVVVVVVVVVVVVHV"
print(output, answer, answer == output)

# input
destination = [15,15]

k = 155117520

# output
output = sol.kthSmallestPath(destination,k)
# answer
answer = "HHHHHHHHHHHHHVHVVVVVVVVVVVVVHV"
print(output, answer, answer == output)
