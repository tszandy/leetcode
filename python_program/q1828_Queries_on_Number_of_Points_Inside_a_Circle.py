from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        return_list = []
        for x_1,y_1,r in queries:
            count = 0
            for x_2,y_2 in points:
                if self.distance(x_1,y_1,x_2,y_2)<=r:
                    count+=1
            return_list.append(count)
        return return_list
                
    def distance(self,x_1,y_1,x_2,y_2):
        return sqrt((x_1-x_2)**2+(y_1-y_2)**2)

sol = Solution()


# input
points = [[1,3],[3,3],[5,3],[2,2]]
queries = [[2,3,1],[4,3,1],[1,1,2]]
# output
output = sol.countPoints(points,queries)
# answer
answer = [3,2,2]
print(output, answer, answer == output)

# input
points = [[1,1],[2,2],[3,3],[4,4],[5,5]]
queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
# output
output = sol.countPoints(points,queries)
# answer
answer = [2,3,2,4]
print(output, answer, answer == output)
