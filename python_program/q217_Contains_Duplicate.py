from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for value in Counter(nums).values():
            if value>=2:
                return True
        return False

sol = Solution()


# input
nums = [1,2,3,1]
# output
output = sol.containsDuplicate(nums)
# answer
answer = True
print(output, answer, answer == output)

# input
nums = [1,2,3,4]
# output
output = sol.containsDuplicate(nums)
# answer
answer = False
print(output, answer, answer == output)

# input
nums = [1,1,1,3,3,4,3,2,4,2]
# output
output = sol.containsDuplicate(nums)
# answer
answer = True
print(output, answer, answer == output)
