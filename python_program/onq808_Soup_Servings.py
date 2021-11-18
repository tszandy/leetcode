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
    # time limit exceed
    def soupServings(self, n: int) -> float:
        return self.soup_servings(n,n)
        
    @lru_cache(None)
    def soup_servings(self,a,b):
        output = 0
        delta_a,delta_b = 100,0
        if   a - delta_a > 0 and b - delta_b > 0:
            operation_output = self.soup_servings(a-delta_a,b-delta_b)
        elif a - delta_a > 0 and b - delta_b <=0:
            operation_output = 0
        elif a - delta_a <=0 and b - delta_b >0:
            operation_output = 1
        elif a - delta_a <=0 and b - delta_b <=0:
            operation_output = 0.5
        output += operation_output

        delta_a,delta_b = 75,25
        if   a - delta_a > 0 and b - delta_b > 0:
            operation_output = self.soup_servings(a-delta_a,b-delta_b)
        elif a - delta_a > 0 and b - delta_b <=0:
            operation_output = 0
        elif a - delta_a <=0 and b - delta_b >0:
            operation_output = 1
        elif a - delta_a <=0 and b - delta_b <=0:
            operation_output = 0.5
        output += operation_output
        
        delta_a,delta_b = 50,50
        if   a - delta_a > 0 and b - delta_b > 0:
            operation_output = self.soup_servings(a-delta_a,b-delta_b)
        elif a - delta_a > 0 and b - delta_b <=0:
            operation_output = 0
        elif a - delta_a <=0 and b - delta_b >0:
            operation_output = 1
        elif a - delta_a <=0 and b - delta_b <=0:
            operation_output = 0.5
        output += operation_output
        
        delta_a,delta_b = 25,75
        if   a - delta_a > 0 and b - delta_b > 0:
            operation_output = self.soup_servings(a-delta_a,b-delta_b)
        elif a - delta_a > 0 and b - delta_b <=0:
            operation_output = 0
        elif a - delta_a <=0 and b - delta_b >0:
            operation_output = 1
        elif a - delta_a <=0 and b - delta_b <=0:
            operation_output = 0.5
        output += operation_output
        
        return 0.25*output
        

sol = Solution()

# input
n = 660295675
# output
output = sol.soupServings(n)
# answer
answer = ""
print(output, answer, answer == output)
