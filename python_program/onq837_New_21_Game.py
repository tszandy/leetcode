from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        store_probability   = defaultdict(float)
        store_probability[0]=1
        
        for i in range(k):
            probability_i = store_probability[i]/maxPts
            for j in range(1,maxPts+1):
                store_probability[i+j]+=probability_i
            del store_probability[i]
        
        success_probability = 0
        fail_probability = 0
        for key,value in store_probability.items():
            if key <=n:
                success_probability += value
            else:
                fail_probability += value
        
        return success_probability
                

sol = Solution()


# input
n = 10
k = 1
maxPts = 10
# output
output = sol.new21Game(n,k,maxPts)
# answer
answer = 1.00000
print(output, answer, answer == output)

# input
n = 6
k = 1
maxPts = 10
# output
output = sol.new21Game(n,k,maxPts)
# answer
answer = 0.60000
print(output, answer, answer == output)

# input
n = 21
k = 17
maxPts = 10
# output
output = sol.new21Game(n,k,maxPts)
# answer
answer = 0.73278
print(output, answer, answer == output)
