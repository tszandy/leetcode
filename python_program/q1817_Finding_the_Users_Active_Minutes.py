from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        store_user_active_min = defaultdict(set)
        for id_num , minute in logs:
            store_user_active_min[id_num].add(minute)
        user_active_minutes_less_k = [0]*k
        for sets in store_user_active_min.values():
            if len(sets)<=k:
                user_active_minutes_less_k[len(sets)-1]+=1
        return user_active_minutes_less_k

sol = Solution()

# input
logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]

k = 5

# output
output = sol.findingUsersActiveMinutes(logs,k)
# answer
answer = [0,2,0,0,0]
print(output, answer, answer == output)

# input
logs = [[1,1],[2,2],[2,3]]

k = 4

# output
output = sol.findingUsersActiveMinutes(logs,k)
# answer
answer = [1,1,0,0]
print(output, answer, answer == output)
