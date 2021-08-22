from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return list(map(lambda x:x+extraCandies>=max(candies),candies))

sol = Solution()


# input
candies = [2,3,5,1,3]
extraCandies = 3
# output
output = sol.kidsWithCandies(candies, extraCandies)
# answer
answer = [True,True,True,False,True] 
print(output, answer, answer == output)

# input
candies = [4,2,1,1,2]
extraCandies = 1
# output
output = sol.kidsWithCandies(candies, extraCandies)
# answer
answer = [True,False,False,False,False] 
print(output, answer, answer == output)

# input
candies = [12,1,12]
extraCandies = 10
# output
output = sol.kidsWithCandies(candies, extraCandies)
# answer
answer = [True,False,True]
print(output, answer, answer == output)
