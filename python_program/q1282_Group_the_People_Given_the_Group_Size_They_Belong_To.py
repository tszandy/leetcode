from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_size_map = defaultdict(list)
        for i,e in enumerate(groupSizes):
            if len(group_size_map[e])==0:
                group_size_map[e].append([i])
            else:
                if len(group_size_map[e][-1])==e:
                    group_size_map[e].append([i])
                else:
                    group_size_map[e][-1].append(i)
        return reduce(lambda x,y:x+y,group_size_map.values())

sol = Solution()

# input
groupSizes = [3,3,3,3,3,1,3]

# output
output = sol.groupThePeople(groupSizes)
# answer
answer = [[0,1,2],[3,4,6],[5]]
print(output, answer, sorted(answer) == sorted(output))

# input
groupSizes = [2,1,3,3,3,2]

# output
output = sol.groupThePeople(groupSizes)
# answer
answer = [[0,5],[1],[2,3,4]]
print(output, answer, sorted(answer) == sorted(output))
