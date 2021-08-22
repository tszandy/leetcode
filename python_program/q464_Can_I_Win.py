from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        n = maxChoosableInteger
        m = desiredTotal
        if n*(n+1)//2<m:
            return False
        range_list = list(range(1,n+1))
        list_1 = range_list[:n//2][::-1]
        list_2 = range_list[n//2:]
        new_list = []
        while list_2 or list_1:
            if list_2:
                new_list.append(list_2.pop())
            if list_1:
                new_list.append(list_1.pop())
            
        count = 0
        for i in range(n):
            count +=new_list.pop(0)
            if m <=count:
                if i %2==0:
                    return True
                else:
                    return False
        

sol = Solution()


# input
maxChoosableInteger = 1

desiredTotal = 0

# output
output = sol.canIWin(maxChoosableInteger,desiredTotal)
# answer
answer = True
print(output, answer, answer == output)

# input
maxChoosableInteger = 1

desiredTotal = 1

# output
output = sol.canIWin(maxChoosableInteger,desiredTotal)
# answer
answer = True
print(output, answer, answer == output)

# input
maxChoosableInteger = 1

desiredTotal = 2

# output
output = sol.canIWin(maxChoosableInteger,desiredTotal)
# answer
answer = False
print(output, answer, answer == output)

# input
maxChoosableInteger = 10

desiredTotal = 11

# output
output = sol.canIWin(maxChoosableInteger,desiredTotal)
# answer
answer = False
print(output, answer, answer == output)

# input
maxChoosableInteger = 10

desiredTotal = 0

# output
output = sol.canIWin(maxChoosableInteger,desiredTotal)
# answer
answer = True
print(output, answer, answer == output)

# input
maxChoosableInteger = 10

desiredTotal = 1

# output
output = sol.canIWin(maxChoosableInteger,desiredTotal)
# answer
answer = True
print(output, answer, answer == output)

# input
maxChoosableInteger = 10

desiredTotal = 1

# output
output = sol.canIWin(maxChoosableInteger,desiredTotal)
# answer
answer = True
print(output, answer, answer == output)

# input
maxChoosableInteger = 20

desiredTotal = 102

# output
output = sol.canIWin(maxChoosableInteger,desiredTotal)
# answer
answer = True
print(output, answer, answer == output)
