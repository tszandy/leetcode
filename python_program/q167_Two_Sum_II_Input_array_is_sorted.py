from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n-1):
            for j in range(i+1,n):
                number = numbers[i]+numbers[j]
                if number== target:
                    return[i+1,j+1]
                if number>target:
                    break


sol = Solution()


# input
numbers = [2,7,11,15]
target = 9
# output
output = sol.twoSum(numbers,target)
# answer
answer = [1,2]
print(output, answer, answer == output)

# input
numbers = [2,3,4]
target = 6
# output
output = sol.twoSum(numbers,target)
# answer
answer = [1,3]
print(output, answer, answer == output)

# input
numbers = [-1,0]
target = -1
# output
output = sol.twoSum(numbers,target)
# answer
answer = [1,2]
print(output, answer, answer == output)

# input
numbers = [0,0,3,4]
target = 0
# output
output = sol.twoSum(numbers,target)
# answer
answer = [1,2]
print(output, answer, answer == output)
