from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations = sorted(citations)
        help_range = range(n,0,-1)
        for i in range(n):
            if help_range[i] <= citations[i]:
                return help_range[i]
        return 0

sol = Solution()


# input
citations = [3,0,6,1,5]
# output
output = sol.hIndex(citations)
# answer
answer = 3
print(output, answer, answer == output)

# input
citations = [1,3,1]
# output
output = sol.hIndex(citations)
# answer
answer = 1
print(output, answer, answer == output)

# input
citations = [0,0]
# output
output = sol.hIndex(citations)
# answer
answer = 0
print(output, answer, answer == output)

# input
citations = [0,0,1]
# output
output = sol.hIndex(citations)
# answer
answer = 1
print(output, answer, answer == output)

# input
citations = [0]
# output
output = sol.hIndex(citations)
# answer
answer = 0
print(output, answer, answer == output)

# input
citations = [1]
# output
output = sol.hIndex(citations)
# answer
answer = 1
print(output, answer, answer == output)

# input
citations = [2]
# output
output = sol.hIndex(citations)
# answer
answer = 1
print(output, answer, answer == output)

# input
citations = [1,2,2,4,5]
# output
output = sol.hIndex(citations)
# answer
answer = 2
print(output, answer, answer == output)
