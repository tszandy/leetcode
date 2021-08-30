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
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.hasApple = hasApple
        self.edge_map = defaultdict(list)
        for node_1,node_2 in edges:
            self.edge_map[node_1].append(node_2)
        return self.path(0)
    
    def path(self,n):
        count_step = 0
        for node in self.edge_map[n]:
            node_count = self.path(node)
            if node_count>0 or (node_count==0 and self.hasApple[node]):
                count_step+=2
            count_step += node_count
        return count_step

sol = Solution()

# input
7
[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
[false,false,true,false,true,true,false]
7
[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
[false,false,true,false,false,true,false]
7
[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
[false,false,false,false,false,false,false]
4
[[0,2],[0,3],[1,2]]
[false,true,false,false]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
