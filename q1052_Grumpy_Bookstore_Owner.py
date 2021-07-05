from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

import numpy as np 
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        customers = np.array(customers)
        grumpy = np.array(grumpy)
        grumpy_list = customers*grumpy
        n = len(customers)
        rolling_grumpy_satisfy = sum(grumpy_list[:minutes])
        max_grumpy_satisfy = rolling_grumpy_satisfy
        for i in range(minutes,n):
            rolling_grumpy_satisfy+= -grumpy_list[i-minutes]+grumpy_list[i]
            max_grumpy_satisfy = max(max_grumpy_satisfy,rolling_grumpy_satisfy)
        none_grumpy_satisfy = sum(customers*(1-grumpy))
        return max_grumpy_satisfy+none_grumpy_satisfy

sol = Solution()


# input
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
# output
output = sol.maxSatisfied(customers,grumpy,minutes)
# answer
answer = 16
print(output, answer, answer == output)
