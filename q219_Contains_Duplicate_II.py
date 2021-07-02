from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        nums_set = set(nums[:k])
        
        if n <= k+1:        
            nums_set = set(nums)
            if len(nums_set)<n:
                return True
            else:
                return False
        
        for i in range(k,n):
            if nums[i] in nums_set:
                return True
            else:
                nums_set.add(nums[i])
                nums_set.remove(nums[i-k])
        return False

sol = Solution()


# input
nums = [1,2,3,1]
k = 3
# output
output = sol.containsNearbyDuplicate(nums,k)
# answer
answer = True
print(output, answer, answer == output)

# input
nums = [1,0,1,1]
k = 1
# output
output = sol.containsNearbyDuplicate(nums,k)
# answer
answer = True
print(output, answer, answer == output)

# input
nums = [1,2,3,1,2,3]
k = 2
# output
output = sol.containsNearbyDuplicate(nums,k)
# answer
answer = False
print(output, answer, answer == output)

# input
nums = [1,1]
k = 3
# output
output = sol.containsNearbyDuplicate(nums,k)
# answer
answer = True
print(output, answer, answer == output)

# input
nums = [1,2]
k = 3
# output
output = sol.containsNearbyDuplicate(nums,k)
# answer
answer = False
print(output, answer, answer == output)
