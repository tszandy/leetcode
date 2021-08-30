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
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.informTime = informTime
        self.manager_to_subordinates = defaultdict(list)
        for subordinate,manager in enumerate(manager):
            self.manager_to_subordinates[manager].append(subordinate)
        return self.num_of_min(headID)
    
    def num_of_min(self,ID):
        max_min = 0
        for subordinate in self.manager_to_subordinates[ID]:
            max_min = max(max_min,self.num_of_min(subordinate))
        return max_min + self.informTime[ID]
        

sol = Solution()

# input
1
0
[-1]
[0]
6
2
[2,2,-1,2,2,2]
[0,0,1,0,0,0]
7
6
[1,2,3,4,5,6,-1]
[0,6,5,4,3,2,1]
15
0
[-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
4
2
[3,3,-1,2]
[0,0,162,914]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
