from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        result = self.predict_the_winner(tuple(nums))
        if result>=0:return True
        else:return False
    
    @lru_cache(None)
    def predict_the_winner(self,nums):
        if len(nums)==1:
            return nums[0]
        return max(nums[0]-self.predict_the_winner(nums[1:]),nums[-1]-self.predict_the_winner(nums[:-1]))

sol = Solution()

# input
nums = [1,1]

# output
output = sol.PredictTheWinner(nums)
# answer
answer = True
print(output, answer, answer == output)

# input
nums = [1,5,2]

# output
output = sol.PredictTheWinner(nums)
# answer
answer = False
print(output, answer, answer == output)

# input
nums = [1,5,233,7]

# output
output = sol.PredictTheWinner(nums)
# answer
answer = True
print(output, answer, answer == output)
