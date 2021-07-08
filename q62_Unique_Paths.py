from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.combination(m-1,m+n-2)

    def combination(self,m,n):
        if m>n:
            return self.combination(n,m)
        if n<(m-n):
            return self.combination(m-n,n)

        count = 1
        for i in range(m+1,n+1):
            count*=i
        for i in range(1,n-m+1):
            count//=i
        return count
# dp 
    def uniquePaths_1(self, m: int, n: int) -> int:
        store_path = {}
        if m ==1 or n == 1:
            return 1
        
        def unique_path(m,n):
            if m ==1 or n == 1:
                return 1
            if m>n:
                m,n=n,m
            if (m,n) in store_path:
                return store_path[(m,n)]
            down = self.uniquePaths(m-1,n)
            right = self.uniquePaths(m,n-1)
            store_path[(m,n)] = down+right
            
            return store_path[(m,n)]

        unique_path(m,n)
        if m>n:
            m,n=n,m

        return store_path[(m,n)]

sol = Solution()


# input
m=3
n=7
# output
output = sol.uniquePaths(m,n)
# answer
answer = 28
print(output, answer, answer == output)

# input
m=2
n=1
# output
output = sol.uniquePaths(m,n)
# answer
answer = 1
print(output, answer, answer == output)

# input
m=7
n=1
# output
output = sol.uniquePaths(m,n)
# answer
answer = 1
print(output, answer, answer == output)

# input
m = 3
n = 2
# output
output = sol.uniquePaths(m,n)
# answer
answer = 3
print(output, answer, answer == output)

# input
m = 7
n = 3
# output
output = sol.uniquePaths(m,n)
# answer
answer = 28
print(output, answer, answer == output)

# input
m = 3
n = 3
# output
output = sol.uniquePaths(m,n)
# answer
answer = 6
print(output, answer, answer == output)

# input
m = 100
n = 3
# output
output = sol.uniquePaths(m,n)
# answer
answer = 5050
print(output, answer, answer == output)

# input
m = 100
n = 4
# output
output = sol.uniquePaths(m,n)
# answer
answer = 171700
print(output, answer, answer == output)

# input
m = 23
n = 12
# output
output = sol.uniquePaths(m,n)
# answer
answer = 193536720
print(output, answer, answer == output)
