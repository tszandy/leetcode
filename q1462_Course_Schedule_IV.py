from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        self.store_prerequisites = np.eye(numCourses)
        
        vertex = list(range(numCourses))
        edge = list(map(lambda x:(x[1],x[0]),prerequisites))
        self.topological_sort(vertex,edge)

        return list(map(lambda x:self.store_prerequisites[x[0],x[1]],queries))

    def topological_sort(self,vertex,edge):
        if len(edge)==0:
            return 
        vertex = set(vertex)
        edge_set = set(map(lambda x:tuple(x),edge))
        edge_map = defaultdict(set)
        edge_map_reverse = defaultdict(set)
        for a,b in edge:
            edge_map[a].add(b)
            edge_map_reverse[b].add(a)

        #set of all nodes with no incoming edge
        s = vertex - reduce(lambda x,y:x.union(y),edge_map.values())
        if len(s)==0:
            return 
        while s:
            node_1 = s.pop()
            for node_2 in edge_map[node_1]:
                edge_set.remove((node_1,node_2))
                edge_map_reverse[node_2].remove(node_1)
                self.store_prerequisites[node_2] = np.logical_or(self.store_prerequisites[node_1],self.store_prerequisites[node_2])
                if len(edge_map_reverse[node_2])==0:
                    s.add(node_2)


sol = Solution()


# input
numCourses = 2

prerequisites = [[1,0]]

queries = [[0,1],[1,0]]

# output
output = sol.checkIfPrerequisite(numCourses,prerequisites,queries)
# answer
answer = [False,True]
print(output, answer, answer == output)

# input
numCourses = 2

prerequisites = []

queries = [[1,0],[0,1]]

# output
output = sol.checkIfPrerequisite(numCourses,prerequisites,queries)
# answer
answer = [False,False]
print(output, answer, answer == output)

# input
numCourses = 3

prerequisites = [[1,2],[1,0],[2,0]]

queries = [[1,0],[1,2]]

# output
output = sol.checkIfPrerequisite(numCourses,prerequisites,queries)
# answer
answer = [True,True]
print(output, answer, answer == output)

# input
numCourses = 2

prerequisites = []

queries = [[1,0],[0,1]]

# output
output = sol.checkIfPrerequisite(numCourses,prerequisites,queries)
# answer
answer = [False,False]
print(output, answer, answer == output)
