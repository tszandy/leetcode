from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        two_people_team = defaultdict(int)
        n = len(rating)
        for j in range(1,n):
            for i in range(j):
                if rating[i]<rating[j]:
                    two_people_team[(j,"g")]+=1
                if rating[i]>rating[j]:
                    two_people_team[(j,"l")]+=1
        count = 0
        for j in range(2,n):
            for i,c in two_people_team:
                if i<j and rating[i]<rating[j] and c=="g":
                    count+=two_people_team[i,c]
                if i<j and rating[i]>rating[j] and c=="l":
                    count+=two_people_team[i,c]
        return count

sol = Solution()


# input
rating = [2,5,3,4,1]

# output
output = sol.numTeams(rating)
# answer
answer = 3
print(output, answer, answer == output)

# input
rating = [2,1,3]

# output
output = sol.numTeams(rating)
# answer
answer = 0
print(output, answer, answer == output)

# input
rating = [1,2,3,4]

# output
output = sol.numTeams(rating)
# answer
answer = 4
print(output, answer, answer == output)

# input
rating = [1,2,3,4]

# output
output = sol.numTeams(rating)
# answer
answer = 4
print(output, answer, answer == output)

# input
rating = [2,5,3,4,1,10,6,8,7,21,30]

# output
output = sol.numTeams(rating)
# answer
answer = 91
print(output, answer, answer == output)
