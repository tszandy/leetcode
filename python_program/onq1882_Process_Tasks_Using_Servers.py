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
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        hq_server = []
        for i,w in enumerate(servers):
            heappush(hq_server,(w,i))
        hq_time = []
        ans = []
        time = 0
        while tasks:
            task = tasks.pop(0)
            
            while not hq_server:
                time +=1
                while hq_time and hq_time[0][0]<=time:
                    t,w,i = heappop(hq_time)
                    heappush(hq_server,(w,i))
            else:
                w,i = heappop(hq_server)
                heappush(hq_time,(time+task,w,i))
                ans.append(i)
                time +=1
                while hq_time and hq_time[0][0]<=time:
                    t,w,i = heappop(hq_time)
                    heappush(hq_server,(w,i))

        return ans

sol = Solution()

# input
servers = [1,2]

tasks = [1,2,3,2,1,2]

# output
output = sol.assignTasks(servers, tasks)
# answer
answer = ""
print(output, answer, answer == output)

# input
servers = [3,3,2]

tasks = [1,2,3,2,1,2]

# output
output = sol.assignTasks(servers, tasks)
# answer
answer = ""
print(output, answer, answer == output)

# input
servers = [5,1,4,3,2]

tasks = [2,1,2,4,5,2,1]

# output
output = sol.assignTasks(servers, tasks)
# answer
answer = ""
print(output, answer, answer == output)
