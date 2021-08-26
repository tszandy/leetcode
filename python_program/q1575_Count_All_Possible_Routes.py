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
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = defaultdict(int)
        n = len(locations)
        dp[(start,fuel)]=1
        count_route = 0
        count_route+=dp[(finish,fuel)]
        count_route%=(10**9+7)
        for i in range(n):
            if i != start:
                j = start
                if fuel-abs(locations[j]-locations[i])>=0:                
                    dp[(i,fuel-abs(locations[j]-locations[i]))]+=1
                
        for f in range(fuel)[::-1]:
            for i in range(n):
                if dp[(i,f)]:
                    for j in range(n):
                        if i!=j and fuel-abs(locations[j]-locations[i])>=0:
                            dp[(j,f-abs(locations[j]-locations[i]))]+=dp[(i,f)]
            count_route+=dp[(finish,f)]
            count_route%=(10**9+7)
        return count_route

    def countRoutes_1(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = defaultdict(int)
        n = len(locations)
        dp[(start,fuel)]=1
        count_route = 0
        count_route+=dp[(finish,fuel)]
        for f in range(fuel)[::-1]:
            for i in range(n):
                for j in range(i+1,n):
                    dp[(i,f)]+=dp[(j,f+abs(locations[j]-locations[i]))]
                    dp[(j,f)]+=dp[(i,f+abs(locations[j]-locations[i]))]
            count_route+=dp[(finish,f)]
        return count_route%(10**9+7)

sol = Solution()

# input
locations = [2,3,6,8,4]

start = 1

finish = 3

fuel = 5

# output
output = sol.countRoutes(locations,start,finish,fuel)
# answer
answer = 4

print(output, answer, answer == output)

# input
locations = [4,3,1]

start = 1

finish = 0

fuel = 6

# output
output = sol.countRoutes(locations,start,finish,fuel)
# answer
answer = 5

print(output, answer, answer == output)

# input
locations = [5,2,1]

start = 0

finish = 2

fuel = 3

# output
output = sol.countRoutes(locations,start,finish,fuel)
# answer
answer = 0

print(output, answer, answer == output)

# input
locations = [2,1,5]

start = 0

finish = 0

fuel = 3

# output
output = sol.countRoutes(locations,start,finish,fuel)
# answer
answer = 2

print(output, answer, answer == output)

# input
locations = [1,2,3]

start = 0

finish = 2

fuel = 40

# output
output = sol.countRoutes(locations,start,finish,fuel)
# answer
answer = 615088286

print(output, answer, answer == output)

# input
locations = [999999993,999999883,999999909,999999971,999999944,999999989,999999935,999999985,999999980,999999929,999999903,999999969,999999879,999999913,999999908,999999894,999999860,999999876,999999958,999999948,999999930,999999918,999999920,999999972,999999862,999999999,999999898,999999926,999999996,999999982,999999998,999999963,999999988,999999854,999999897,999999852,999999936,999999915,999999900,999999850,999999882,999999902,999999934,999999970,999999991,999999853,999999984,999999975,999999872,999999928,999999856,999999957,999999931,999999888,999999924,999999949,999999893,999999943,999999857,999999977,999999912,999999974,999999981]

start = 37

finish = 14

fuel = 62

# output
output = sol.countRoutes(locations,start,finish,fuel)
# answer
answer = 58377110
print(output, answer, answer == output)
