from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n)[::-1]:
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]=digits[i]+1
                return digits
        digits.insert(0,1)
        return digits

sol = Solution()


# input
digits = [1,2,3]
# output
output = sol.plusOne(digits)
# answer
answer = [1,2,4]
print(output, answer, answer == output)

# input
digits = [4,3,2,1]
# output
output = sol.plusOne(digits)
# answer
answer = [4,3,2,2]
print(output, answer, answer == output)

# input
digits = [0]
# output
output = sol.plusOne(digits)
# answer
answer = [1]
print(output, answer, answer == output)

# input
digits = [9,9]
# output
output = sol.plusOne(digits)
# answer
answer = [1,0,0]
print(output, answer, answer == output)
