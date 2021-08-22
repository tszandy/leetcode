from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def twoEggDrop(self, n: int) -> int:
        return floor(sqrt((n-2)*2+9/4)-1/2)+1

sol = Solution()


# input
n = 1
# output
output = sol.twoEggDrop(n)
# answer
answer = 1
print(output, answer, answer == output)

# input
n = 2
# output
output = sol.twoEggDrop(n)
# answer
answer = 2
print(output, answer, answer == output)

# input
n = 3
# output
output = sol.twoEggDrop(n)
# answer
answer = 2
print(output, answer, answer == output)

# input
n = 4
# output
output = sol.twoEggDrop(n)
# answer
answer = 3
print(output, answer, answer == output)

# input
n = 6
# output
output = sol.twoEggDrop(n)
# answer
answer = 3
print(output, answer, answer == output)

# input
n = 7
# output
output = sol.twoEggDrop(n)
# answer
answer = 4
print(output, answer, answer == output)

# input
n = 10
# output
output = sol.twoEggDrop(n)
# answer
answer = 4
print(output, answer, answer == output)

# input
n = 11
# output
output = sol.twoEggDrop(n)
# answer
answer = 5
print(output, answer, answer == output)

# input
n = 15
# output
output = sol.twoEggDrop(n)
# answer
answer = 5
print(output, answer, answer == output)

# input
n = 16
# output
output = sol.twoEggDrop(n)
# answer
answer = 6
print(output, answer, answer == output)

# input
n = 21
# output
output = sol.twoEggDrop(n)
# answer
answer = 6
print(output, answer, answer == output)

# input
n = 22
# output
output = sol.twoEggDrop(n)
# answer
answer = 7
print(output, answer, answer == output)

# input
n = 100
# output
output = sol.twoEggDrop(n)
# answer
answer = 14
print(output, answer, answer == output)
