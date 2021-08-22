from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        difference = []
        n = len(timePoints)
        time_minutes = list(map(lambda x:int(x[0])*60+int(x[1]),map(lambda x:x.split(":"),timePoints)))
        for i in range(n):
            for j in range(i+1,n):
                delta = abs(time_minutes[i]-time_minutes[j])
                if delta == 0:
                    return 0
                difference.append(min(delta,1440-delta))
        return min(difference)

sol = Solution()


# input
timePoints = ["23:59","00:00"]
# output
output = sol.findMinDifference(timePoints)
# answer
answer = 1
print(output, answer, answer == output)

# input
timePoints = ["00:00","23:59","00:00"]
# output
output = sol.findMinDifference(timePoints)
# answer
answer = 0
print(output, answer, answer == output)
