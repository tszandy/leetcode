from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        vertex = list(range(numCourses))
        edge = prerequisites
        return_list = self.topological_sort(vertex,edge)
        if return_list:
            return True
        else:
            return False
        
    def topological_sort(self,vertex,edge):
        if len(edge)==0:
            return list(vertex)

        vertex = set(vertex)
        return_list = []
        edge_set = set(map(lambda x:tuple(x),edge))
        edge_map = defaultdict(set)
        edge_map_reverse = defaultdict(set)
        for a,b in edge:
            edge_map[a].add(b)
            edge_map_reverse[b].add(a)

        #set of all nodes with no incoming edge
        s = vertex - reduce(lambda x,y:x.union(y),edge_map.values())
        if len(s)==0:
            return return_list
        while s:
            node_1 = s.pop()
            return_list.append(node_1)
            for node_2 in edge_map[node_1]:
                edge_set.remove((node_1,node_2))
                edge_map_reverse[node_2].remove(node_1)
                if len(edge_map_reverse[node_2])==0:
                    s.add(node_2)
        if len(edge_set)==0:
            return return_list
        else:
            return []


sol = Solution()


# input
numCourses = 1

prerequisites = []

# output
output = sol.canFinish(numCourses,prerequisites)
# answer
answer = True
print(output, answer, answer == output)

# input
numCourses = 2

prerequisites = [[1,0]]

# output
output = sol.canFinish(numCourses,prerequisites)
# answer
answer = True
print(output, answer, answer == output)

# input
numCourses = 2

prerequisites = [[1,0],[0,1]]

# output
output = sol.canFinish(numCourses,prerequisites)
# answer
answer = False
print(output, answer, answer == output)

# input
numCourses = 8

prerequisites = [[3,0],[5,3],[3,1],[6,3],[6,4],[4,1],[3,2],[7,4],[7,2]]

# output
output = sol.canFinish(numCourses,prerequisites)
# answer
answer = True
print(output, answer, answer == output)

# input
numCourses = 8

prerequisites = [[3,0],[5,3],[3,1],[6,3],[4,6],[3,4],[4,1],[3,2],[7,4],[7,2]]

# output
output = sol.canFinish(numCourses,prerequisites)
# answer
answer = False
print(output, answer, answer == output)
