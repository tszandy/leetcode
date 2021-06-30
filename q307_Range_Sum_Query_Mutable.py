from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

import numpy as np
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cum_sum = np.cumsum(nums)

    def update(self, index: int, val: int) -> None:
        self.cum_sum[index:]+=(val-self.nums[index])
        self.nums[index]=val

    def sumRange(self, left: int, right: int) -> int:
        sum_range = 0
        sum_range+=self.cum_sum[right]
        if left != 0:
            sum_range-=self.cum_sum[left-1]
        return sum_range

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

sol = Solution()


# input

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
