from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0 :
            return 0
        dp_left_max = [0]*n
        dp_right_max = [0]*n
        dp_left_max[0] = height[0]
        for i in range(1,n):
            if dp_left_max[i-1]<height[i]:
                dp_left_max[i] = height[i]
            else:
                dp_left_max[i] = dp_left_max[i-1]
        
        dp_right_max[n-1] = height[n-1]
        for i in range(n-1)[::-1]:
            if height[i]>dp_right_max[i+1]:
                dp_right_max[i] = height[i]
            else:
                dp_right_max[i] = dp_right_max[i+1]

        count_water = 0
        
        for i in range(n):
            count_water+=min(dp_left_max[i],dp_right_max[i])-height[i]
        
        return count_water


sol = Solution()


# input
height = [0,1,0,2,1,0,1,3,2,1,2,1]
# output
output = sol.trap(height)
# answer
answer = 6
print(output, answer, answer == output)

# input
height = [4,2,0,3,2,5]
# output
output = sol.trap(height)
# answer
answer = 9
print(output, answer, answer == output)

# input
height = []
# output
output = sol.trap(height)
# answer
answer = 0
print(output, answer, answer == output)

# input
height = [1]
# output
output = sol.trap(height)
# answer
answer = 0
print(output, answer, answer == output)

# input
height = [2,0]
# output
output = sol.trap(height)
# answer
answer = 0
print(output, answer, answer == output)

# input
height = [2,0,1]
# output
output = sol.trap(height)
# answer
answer = 1
print(output, answer, answer == output)
