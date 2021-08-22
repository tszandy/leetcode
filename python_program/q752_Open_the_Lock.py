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
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        up = lambda x:str(int(x)+1)[-1]
        down = lambda x:str(int(x)+9)[-1]
        wheel_list = ["0000"]
        count_step = 0
        visited = set()
        while wheel_list:
            next_list = []
            for wheel in wheel_list:
                if wheel in deadends:
                    break
                if wheel == target:
                    return count_step
                for i in range(4):
                    next_wheel = wheel[:i]+up(wheel[i])+wheel[i+1:]
                    if next_wheel not in visited and next_wheel not in deadends:
                        next_list.append(next_wheel)
                        visited.add(next_wheel)
                    next_wheel = wheel[:i]+down(wheel[i])+wheel[i+1:]
                    if next_wheel not in visited and next_wheel not in deadends:
                        next_list.append(next_wheel)
                        visited.add(next_wheel)
            wheel_list = next_list
            count_step +=1
        return -1

sol = Solution()

# input
deadends = ["0201","0101","0102","1212","2002"]

target = "0202"

# output
output = sol.openLock(deadends,target)
# answer
answer = 6
print(output, answer, answer == output)

# input
deadends = ["8888"]

target = "0009"

# output
output = sol.openLock(deadends,target)
# answer
answer = 1
print(output, answer, answer == output)

# input
deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]

target = "8888"

# output
output = sol.openLock(deadends,target)
# answer
answer = -1
print(output, answer, answer == output)

# input
deadends = ["0000"]

target = "8888"

# output
output = sol.openLock(deadends,target)
# answer
answer = -1
print(output, answer, answer == output)
