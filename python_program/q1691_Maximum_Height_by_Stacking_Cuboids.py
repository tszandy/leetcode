from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)
        cuboids = sorted(map(lambda x:sorted(x),cuboids),key = lambda x:(x[2],x[1],x[0]))
        max_height_index = {}
        for i in range(n):
            cuboid_a = cuboids[i]
            max_height = cuboid_a[2]
            for j in range(i):
                cuboid_b = cuboids[j]
                if cuboid_b[0]<=cuboid_a[0] and cuboid_b[1]<=cuboid_a[1] and cuboid_b[2]<=cuboid_a[2]:
                    max_height = max(max_height,cuboid_a[2]+max_height_index[j])
            max_height_index[i]=max_height
        return max(max_height_index.values())

sol = Solution()


# input
cuboids = [[50,45,20],[95,37,53],[45,23,12]]
# output
output = sol.maxHeight(cuboids)
# answer
answer = 190
print(output, answer, answer == output)

# input
cuboids = [[38,25,45],[76,35,3]]
# output
output = sol.maxHeight(cuboids)
# answer
answer = 76
print(output, answer, answer == output)

# input
cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
# output
output = sol.maxHeight(cuboids)
# answer
answer = 102
print(output, answer, answer == output)
