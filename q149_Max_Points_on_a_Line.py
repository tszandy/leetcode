from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        line_count = defaultdict(int)
        for i in range(n-1):
            for j in range(i+1,n):
                point_1 = points[i]
                point_2 = points[j]
                line_count[self.line(point_1,point_2)]+=1
        max_val = max(line_count.values())
        return int(sqrt(2*max_val+1/2)+1/2)
        
    def line(self,point_1,point_2):
        if point_1[0]==point_2[0]:
            return "x="+str(point_1[0])
        if point_1[1]==point_2[1]:
            return "y="+str(point_1[1])
        
        a = ((point_2[1]-point_1[1]),(point_2[0]-point_1[0]))
        gcd_a = gcd(*a)
        a= (int(a[0]/gcd_a),int(a[1]/gcd_a))
        if a[1]<0:
            a = (-a[0],-a[1])
        b = (a[1]*point_2[1]-a[0]*point_2[0],a[1])
        gcd_b = gcd(*b)
        b= (int(b[0]/gcd_b),int(b[1]/gcd_b))
        if b[1]<0:
            b = (-b[0],-b[1])
        
        return (a,b)

sol = Solution()


# input
points = [[0,0]]
# output
output = sol.maxPoints(points)
# answer
answer = 1
print(output, answer, answer == output)

# input
points = [[1,1],[2,2],[3,3]]
# output
output = sol.maxPoints(points)
# answer
answer = 3
print(output, answer, answer == output)

# input
points = [[2,3],[3,3],[-5,3]]
# output
output = sol.maxPoints(points)
# answer
answer = 3
print(output, answer, answer == output)

# input
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# output
output = sol.maxPoints(points)
# answer
answer = 4
print(output, answer, answer == output)

# input
points = [[0,1],[0,2],[0,3]]
# output
output = sol.maxPoints(points)
# answer
answer = 3
print(output, answer, answer == output)

# input
points = [[-6,-1],[3,1],[12,3]]
# output
output = sol.maxPoints(points)
# answer
answer = 3
print(output, answer, answer == output)
