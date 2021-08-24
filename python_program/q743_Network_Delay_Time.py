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
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edge_map = defaultdict(list)
        max_time = 0
        visited = set([k])
        for s,t,w in times:
            edge_map[s].append((t,w))
        path_list = [(k,0)]
        while path_list:
            next_list = []
            for s,w_1 in path_list:
                for t,w_2 in edge_map[s]:
                    if t not in visited:
                        max_time = max(max_time,w_1+w_2)
                        next_list.append((t,w_1+w_2))
                        visited.add(t)
            path_list = next_list
        if len(visited)!=n:
            return -1
        else:
            return max_time

sol = Solution()

# input
times = [[2,1,1],[2,3,1],[3,4,1]]

n = 4

k = 2

# output
output = sol.networkDelayTime(times,n,k)
# answer
answer = 2

print(output, answer, answer == output)

# input
times = [[1,2,1]]

n = 2

k = 1

# output
output = sol.networkDelayTime(times,n,k)
# answer
answer = 1

print(output, answer, answer == output)

# input
times = [[1,2,1]]

n = 2

k = 2

# output
output = sol.networkDelayTime(times,n,k)
# answer
answer = -1

print(output, answer, answer == output)

# input
times = [[1,2,1],[2,3,2],[1,3,4]]

n = 3

k = 1

# output
output = sol.networkDelayTime(times,n,k)
# answer
answer = 3

print(output, answer, answer == output)
