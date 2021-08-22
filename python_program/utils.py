from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
import heapq
from bisect import bisect_left

class MaxHeap:
    def __init__(self,data):
        self.data = list(map(lambda x:-x,data))
        heapq.heapify(self.data)
    def __init__(self):
        self.data = []

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)
    def size(self):
        return len(self.data)


def topological_sort(vertex,edge):
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
