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
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        count = [1]*n
        ans = [0]*n
        
        def count_sub_tree_and_score(node , parent = None):
            for child in graph[node]:
                if child != parent:
                    count_sub_tree_and_score(child,node)
                    count[node] += count[child]
                    ans[node] += ans[child]+count[child]
        def propagate_score(node,parent = None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node]- count[child] + n -count[child]
                    propagate_score(child,node)
        
        count_sub_tree_and_score(0)
        propagate_score(0)
        return ans

sol = Solution()

# input
n = 6

edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]

# output
output = sol.sumOfDistancesInTree(n,edges)
# answer
answer = [8,12,6,10,10,10]

print(output, answer, answer == output)

# input
n = 1

edges = []

# output
output = sol.sumOfDistancesInTree(n,edges)
# answer
answer = [0]

print(output, answer, answer == output)

# input
n = 2

edges = [[1,0]]

# output
output = sol.sumOfDistancesInTree(n,edges)
# answer
answer = [1,1]

print(output, answer, answer == output)
