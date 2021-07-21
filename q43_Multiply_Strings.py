from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        map_str_to_int = lambda x_1:reduce(lambda y,z:10*y+z,map(lambda x:ord(x)-48,x_1))
        return str(map_str_to_int(num1)*map_str_to_int(num2))


sol = Solution()


# input
num1 = "0"

num2 = "3"

# output
output = sol.multiply(num1,num2)
# answer
answer = "0"
print(output, answer, answer == output)

# input
num1 = "2"

num2 = "3"

# output
output = sol.multiply(num1,num2)
# answer
answer = "6"
print(output, answer, answer == output)

# input
num1 = "123"

num2 = "456"

# output
output = sol.multiply(num1,num2)
# answer
answer = "56088"
print(output, answer, answer == output)
