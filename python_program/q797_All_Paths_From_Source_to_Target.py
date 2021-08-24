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
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = [[0]]
        return_paths = []
        while paths:
            next_paths = []
            for path in paths:
                last_node = path[-1]
                if last_node == n-1:
                    return_paths.append(path)
                    continue
                for node in graph[last_node]:
                    next_paths.append(path+[node])
            paths = next_paths
        return return_paths
        

sol = Solution()

# input
graph = [[1,2],[3],[3],[]]

# output
output = sol.allPathsSourceTarget(graph)
# answer
answer = [[0,1,3],[0,2,3]]

print(output, answer, answer == output)

# input
graph = [[4,3,1],[3,2,4],[3],[4],[]]

# output
output = sol.allPathsSourceTarget(graph)
# answer
answer = [[0,4],[0,3,4],[0,1,4],[0,1,3,4],[0,1,2,3,4]]

print(output, answer, answer == output)

# input
graph = [[1],[]]

# output
output = sol.allPathsSourceTarget(graph)
# answer
answer = [[0,1]]

print(output, answer, answer == output)

# input
graph = [[1,2,3],[2],[3],[]]

# output
output = sol.allPathsSourceTarget(graph)
# answer
answer = [[0,3],[0,2,3],[0,1,2,3]]

print(output, answer, answer == output)

# input
graph = [[1,3],[2],[3],[]]

# output
output = sol.allPathsSourceTarget(graph)
# answer
answer = [[0,3],[0,1,2,3]]

print(output, answer, answer == output)
