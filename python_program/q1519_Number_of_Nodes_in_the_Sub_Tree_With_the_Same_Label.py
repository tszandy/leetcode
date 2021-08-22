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
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        q = queue.Queue()
        for edge in edges:
            q.put(edge)
        
        label_map = defaultdict(lambda :defaultdict(int))
        visited_set = set([0])
        edges = []
        while q.qsize():
            node_1,node_2 = q.get()
            if node_1 not in visited_set and node_2 not in visited_set:
                q.put((node_1,node_2))
            elif node_1 in visited_set:
                edges.append((node_1,node_2))
                visited_set.add(node_2)
            else:
                edges.append((node_2,node_1))
                visited_set.add(node_1)
                
        for i in range(n):
            label_map[i][labels[i]]+=1

        for node_1,node_2 in edges[::-1]:
            for k,v in label_map[node_2].items():
                label_map[node_1][k]+=v
        
        return_list = []
        for i in range(n):
            return_list.append(label_map[i][labels[i]])
        return return_list
sol = Solution()

# input
n = 7

edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]

labels = "abaedcd"

# output
output = sol.countSubTrees(n,edges,labels)
# answer
answer = [2,1,1,1,1,1,1]

print(output, answer, answer == output)

# input
n = 4
edges = [[0,1],[1,2],[0,3]]
labels = "bbbb"

# output
output = sol.countSubTrees(n,edges,labels)
# answer
answer = [4,2,1,1]

print(output, answer, answer == output)

# input
n = 5

edges = [[0,1],[0,2],[1,3],[0,4]]

labels = "aabab"

# output
output = sol.countSubTrees(n,edges,labels)
# answer
answer = [3,2,1,1,1]

print(output, answer, answer == output)

# input
n = 6

edges = [[0,1],[0,2],[1,3],[3,4],[4,5]]

labels = "cbabaa"

# output
output = sol.countSubTrees(n,edges,labels)
# answer
answer = [1,2,1,1,2,1]

print(output, answer, answer == output)

# input
n = 7

edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]]

labels = "aaabaaa"

# output
output = sol.countSubTrees(n,edges,labels)
# answer
answer = [6,5,4,1,3,2,1]

print(output, answer, answer == output)

# input
n = 4

edges = [[0,2],[0,3],[1,2]]

labels = "aeed"

# output
output = sol.countSubTrees(n,edges,labels)
# answer
answer = [1,1,2,1]

print(output, answer, answer == output)

# input
n = 4

edges = [[1,2],[0,2],[0,3]]

labels = "aeed"

# output
output = sol.countSubTrees(n,edges,labels)
# answer
answer = [1,1,2,1]

print(output, answer, answer == output)

# input
n = 25

edges = [[4,0],[5,4],[12,5],[3,12],[18,3],[10,18],[8,5],[16,8],[14,16],[13,16],[9,13],[22,9],[2,5],[6,2],[1,6],[11,1],[15,11],[20,11],[7,20],[19,1],[17,19],[23,19],[24,2],[21,24]]

labels = "hcheiavadwjctaortvpsflssg"

# output
output = sol.countSubTrees(n,edges,labels)
# answer
answer = [2,2,1,1,1,3,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]

print(output, answer, answer == output)
