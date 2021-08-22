from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        vertexs = list(map(lambda x:(x[0],x[1]),points))
        weighted_edges = defaultdict(list)
        for i in range(len(vertexs)-1):
            for j in range(i+1,len(vertexs)):
                point_1 = vertexs[i]
                point_2 = vertexs[j]
                distance = self.manhattan_distance(point_1,point_2)
                weighted_edges[point_1].append((distance,(point_1,point_2)))
                weighted_edges[point_2].append((distance,(point_2,point_1)))
        return sum(map(lambda x:x[0],self.minimum_spaning_tree(vertexs,weighted_edges)))
                
    def minimum_spaning_tree(self,vertexs,weighted_edges):
        start_vertex = vertexs[0]
        visited_vertexs = set()
        hq = []
        visited_vertexs.add(start_vertex)
        for weighted_edge in weighted_edges[start_vertex]:
            heappush(hq, weighted_edge)
        minimum_spaning_tree_edge_list = []
        while True:
            if len(visited_vertexs)!=len(vertexs):
                cost,(point1,point2) = heappop(hq)
                if point2 not in visited_vertexs:
                    visited_vertexs.add(point2)
                    minimum_spaning_tree_edge_list.append((cost,(point1,point2)))
                    for weighted_edge in weighted_edges[point2]:
                        if weighted_edge[1][1] not in visited_vertexs:
                            heappush(hq, weighted_edge)
            else:
                break
        return minimum_spaning_tree_edge_list
    
    def manhattan_distance(self,a,b):
        return abs(a[0]-b[0])+abs(a[1]-b[1])

sol = Solution()


# input
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# output
output = sol.minCostConnectPoints(points)
# answer
answer = 20
print(output, answer, answer == output)

# input
points = [[3,12],[-2,5],[-4,1]]
# output
output = sol.minCostConnectPoints(points)
# answer
answer = 18
print(output, answer, answer == output)

# input
points = [[0,0],[1,1],[1,0],[-1,1]]
# output
output = sol.minCostConnectPoints(points)
# answer
answer = 4
print(output, answer, answer == output)

# input
points = [[0,0],[1,1]]
# output
output = sol.minCostConnectPoints(points)
# answer
answer = 2
print(output, answer, answer == output)

# input
points = [[-1000000,-1000000],[1000000,1000000]]
# output
output = sol.minCostConnectPoints(points)
# answer
answer = 4000000
print(output, answer, answer == output)

# input
points = [[0,0]]
# output
output = sol.minCostConnectPoints(points)
# answer
answer = 0
print(output, answer, answer == output)
