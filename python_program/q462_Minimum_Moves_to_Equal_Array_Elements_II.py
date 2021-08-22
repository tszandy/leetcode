from typing import List

import numpy as np 
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums=sorted(nums)
        median = round(np.median(nums))
        return sum(map(lambda x:abs(x-median),nums))

sol = Solution()

print(sol.minMoves2())